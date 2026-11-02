import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Router, provideRouter } from '@angular/router';

import { AuthService } from '../../auth/auth.service';
import { ShellComponent } from './shell.component';

describe('ShellComponent', () => {
  let fixture: ComponentFixture<ShellComponent>;
  const authService = { signOut: vi.fn() };

  beforeEach(async () => {
    authService.signOut.mockReset().mockResolvedValue(undefined);
    await TestBed.configureTestingModule({
      imports: [ShellComponent],
      providers: [provideRouter([]), { provide: AuthService, useValue: authService }],
    }).compileComponents();

    fixture = TestBed.createComponent(ShellComponent);
    fixture.detectChanges();
  });

  it('shows a Logout button in the toolbar', () => {
    const button = (fixture.nativeElement as HTMLElement).querySelector('mat-toolbar .logout-btn');
    expect(button?.textContent).toContain('Logout');
  });

  it('signs out and returns to /login when Logout is clicked', async () => {
    const navigate = vi.spyOn(TestBed.inject(Router), 'navigate').mockResolvedValue(true);

    ((fixture.nativeElement as HTMLElement).querySelector('.logout-btn') as HTMLButtonElement).click();
    await fixture.whenStable();

    expect(authService.signOut).toHaveBeenCalledTimes(1);
    expect(navigate).toHaveBeenCalledWith(['/login'], { replaceUrl: true });
  });
});
