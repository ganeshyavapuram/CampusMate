import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';

import { environment } from '../../../../environments/environment';
import { DashboardPage } from './dashboard.page';

describe('DashboardPage', () => {
  let http: HttpTestingController;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DashboardPage],
      providers: [provideHttpClient(), provideHttpClientTesting()],
    }).compileComponents();
    http = TestBed.inject(HttpTestingController);
  });

  afterEach(() => http.verify());

  function statusAfter(respond: (req: ReturnType<HttpTestingController['expectOne']>) => void): string | null | undefined {
    const fixture = TestBed.createComponent(DashboardPage);
    fixture.detectChanges();
    respond(http.expectOne(`${environment.apiBaseUrl}/health`));
    fixture.detectChanges();
    return (fixture.nativeElement as HTMLElement).querySelector('[data-testid="backend-status"]')?.textContent;
  }

  it('shows the status returned by the back end', () => {
    expect(statusAfter((req) => req.flush({ status: 'ok' }))).toBe('ok');
  });

  it('says the back end is unreachable when the request fails', () => {
    expect(statusAfter((req) => req.error(new ProgressEvent('error')))).toBe('unreachable');
  });
});
