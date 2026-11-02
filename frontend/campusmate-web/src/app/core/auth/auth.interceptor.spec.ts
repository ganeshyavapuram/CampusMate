import { HttpClient, provideHttpClient, withInterceptors } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';
import { firstValueFrom } from 'rxjs';

import { environment } from '../../../environments/environment';
import { authInterceptor } from './auth.interceptor';
import { AuthService } from './auth.service';

describe('authInterceptor', () => {
  const authService = { getIdToken: vi.fn() };
  let http: HttpClient;
  let httpTesting: HttpTestingController;

  beforeEach(() => {
    authService.getIdToken.mockReset();
    TestBed.configureTestingModule({
      providers: [
        provideHttpClient(withInterceptors([authInterceptor])),
        provideHttpClientTesting(),
        { provide: AuthService, useValue: authService },
      ],
    });
    http = TestBed.inject(HttpClient);
    httpTesting = TestBed.inject(HttpTestingController);
  });

  afterEach(() => httpTesting.verify());

  // The token lookup is async, so wait a tick before the request reaches the testing backend.
  const flushMicrotasks = () => new Promise((resolve) => setTimeout(resolve));

  it('adds the Bearer token to API requests when signed in', async () => {
    authService.getIdToken.mockResolvedValue('test-token');
    const response = firstValueFrom(http.get(`${environment.apiBaseUrl}/health`));
    await flushMicrotasks();

    const req = httpTesting.expectOne(`${environment.apiBaseUrl}/health`);
    expect(req.request.headers.get('Authorization')).toBe('Bearer test-token');
    req.flush({ status: 'ok' });
    await response;
  });

  it('sends API requests without the header when signed out', async () => {
    authService.getIdToken.mockResolvedValue(null);
    const response = firstValueFrom(http.get(`${environment.apiBaseUrl}/health`));
    await flushMicrotasks();

    const req = httpTesting.expectOne(`${environment.apiBaseUrl}/health`);
    expect(req.request.headers.has('Authorization')).toBe(false);
    req.flush({ status: 'ok' });
    await response;
  });

  it('never adds the token to requests for other hosts', async () => {
    const response = firstValueFrom(http.get('https://example.com/data'));

    const req = httpTesting.expectOne('https://example.com/data');
    expect(req.request.headers.has('Authorization')).toBe(false);
    expect(authService.getIdToken).not.toHaveBeenCalled();
    req.flush({});
    await response;
  });
});
