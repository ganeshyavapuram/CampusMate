import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Router, provideRouter } from '@angular/router';

import { AuthService } from '../../../core/auth/auth.service';
import { LoginComponent } from './login.component';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;
  const authService = { signInWithGoogle: vi.fn() };

  beforeEach(async () => {
    authService.signInWithGoogle.mockReset();
    await TestBed.configureTestingModule({
      imports: [LoginComponent],
      providers: [provideRouter([]), { provide: AuthService, useValue: authService }],
    }).compileComponents();

    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('creates the component', () => {
    expect(component).toBeTruthy();
  });

  it('renders the CampusMate title', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    const title = compiled.querySelector('mat-card-title');
    expect(title?.textContent?.trim()).toBe('CampusMate');
  });

  it('shows an introduction paragraph about CampusMate', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    const description = compiled.querySelector('.description');
    expect(description?.textContent).toContain('Manage your subjects, timetable, assignments, attendance, and study plans');
  });

  it('displays the "Sign in with Google" button', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    const button = compiled.querySelector('.google-signin-btn');
    expect(button).toBeTruthy();
    expect(button?.textContent).toContain('Sign in with Google');
  });

  async function clickSignIn(): Promise<HTMLElement> {
    const compiled = fixture.nativeElement as HTMLElement;
    (compiled.querySelector('.google-signin-btn') as HTMLButtonElement).click();
    await fixture.whenStable();
    fixture.detectChanges();
    return compiled;
  }

  it('goes to the dashboard after a successful Google sign-in', async () => {
    authService.signInWithGoogle.mockResolvedValue('signed-in');
    const navigate = vi.spyOn(TestBed.inject(Router), 'navigate').mockResolvedValue(true);

    await clickSignIn();

    expect(authService.signInWithGoogle).toHaveBeenCalledTimes(1);
    expect(navigate).toHaveBeenCalledWith(['/dashboard']);
  });

  it('stays on the login page and shows a message when the popup is closed', async () => {
    authService.signInWithGoogle.mockResolvedValue('cancelled');
    const navigate = vi.spyOn(TestBed.inject(Router), 'navigate');

    const compiled = await clickSignIn();

    expect(navigate).not.toHaveBeenCalled();
    expect(compiled.querySelector('.signin-message')?.textContent?.trim()).toBe('Sign-in was cancelled.');
  });

  it('tells the student to allow pop-ups when the browser blocks the popup', async () => {
    authService.signInWithGoogle.mockResolvedValue('popup-blocked');

    const compiled = await clickSignIn();

    expect(compiled.querySelector('.signin-message')?.textContent).toContain('Allow pop-ups for this site');
  });

  it('shows an error message when sign-in fails', async () => {
    authService.signInWithGoogle.mockRejectedValue(new Error('network'));

    const compiled = await clickSignIn();

    expect(compiled.querySelector('.signin-message')?.textContent?.trim()).toBe('Sign-in failed. Please try again.');
  });
});
