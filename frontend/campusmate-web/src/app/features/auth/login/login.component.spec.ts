import { ComponentFixture, TestBed } from '@angular/core/testing';
import { LoginComponent } from './login.component';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LoginComponent],
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
});
