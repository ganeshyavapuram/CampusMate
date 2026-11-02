import { TestBed } from '@angular/core/testing';
import { ActivatedRouteSnapshot, Router, RouterStateSnapshot, UrlTree, provideRouter } from '@angular/router';

import { authGuard } from './auth.guard';
import { AuthService } from './auth.service';

describe('authGuard', () => {
  const authService = { isSignedIn: vi.fn() };

  beforeEach(() => {
    authService.isSignedIn.mockReset();
    TestBed.configureTestingModule({
      providers: [provideRouter([]), { provide: AuthService, useValue: authService }],
    });
  });

  const runGuard = () =>
    TestBed.runInInjectionContext(() =>
      authGuard({} as ActivatedRouteSnapshot, {} as RouterStateSnapshot),
    ) as Promise<boolean | UrlTree>;

  it('lets a signed-in student through', async () => {
    authService.isSignedIn.mockResolvedValue(true);
    await expect(runGuard()).resolves.toBe(true);
  });

  it('redirects a signed-out visitor to /login', async () => {
    authService.isSignedIn.mockResolvedValue(false);
    const result = await runGuard();
    const router = TestBed.inject(Router);
    expect(router.serializeUrl(result as UrlTree)).toBe('/login');
  });
});
