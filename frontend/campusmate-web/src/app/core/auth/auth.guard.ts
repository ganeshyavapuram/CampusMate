import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';

import { AuthService } from './auth.service';

/** Lets signed-in students through; sends everyone else to /login. */
export const authGuard: CanActivateFn = async () => {
  const authService = inject(AuthService);
  const router = inject(Router);

  return (await authService.isSignedIn()) || router.createUrlTree(['/login']);
};
