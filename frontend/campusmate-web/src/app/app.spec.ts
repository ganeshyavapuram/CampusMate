import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';

import { App } from './app';
import { environment } from '../environments/environment';

describe('App', () => {
  let http: HttpTestingController;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
      providers: [provideHttpClient(), provideHttpClientTesting()],
    }).compileComponents();
    http = TestBed.inject(HttpTestingController);
  });

  afterEach(() => http.verify());

  it('renders the CampusMate title', () => {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();
    http.expectOne(`${environment.apiBaseUrl}/health`).flush({ status: 'ok' });
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('h1')?.textContent).toContain('CampusMate');
  });

  it('shows the status returned by the back end', () => {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();
    http.expectOne(`${environment.apiBaseUrl}/health`).flush({ status: 'ok' });
    fixture.detectChanges();
    const status = (fixture.nativeElement as HTMLElement).querySelector('[data-testid="backend-status"]');
    expect(status?.textContent).toBe('ok');
  });

  it('says the back end is unreachable when the request fails', () => {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();
    http.expectOne(`${environment.apiBaseUrl}/health`).error(new ProgressEvent('error'));
    fixture.detectChanges();
    const status = (fixture.nativeElement as HTMLElement).querySelector('[data-testid="backend-status"]');
    expect(status?.textContent).toBe('unreachable');
  });
});
