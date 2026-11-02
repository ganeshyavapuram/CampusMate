import { TestBed } from '@angular/core/testing';
import { UserCredential } from 'firebase/auth';

import { AuthService } from './auth.service';

describe('AuthService', () => {
  let service: AuthService;
  let openPopup: ReturnType<typeof vi.spyOn>;

  beforeEach(() => {
    service = TestBed.inject(AuthService);
    openPopup = vi.spyOn(service as unknown as { openGooglePopup: () => Promise<UserCredential> }, 'openGooglePopup');
  });

  it('returns "signed-in" when the Google popup succeeds', async () => {
    openPopup.mockResolvedValue({} as UserCredential);
    await expect(service.signInWithGoogle()).resolves.toBe('signed-in');
  });

  it('returns "cancelled" when the student closes the popup', async () => {
    openPopup.mockRejectedValue({ code: 'auth/popup-closed-by-user' });
    await expect(service.signInWithGoogle()).resolves.toBe('cancelled');
  });

  it('returns "popup-blocked" when the browser blocks the popup', async () => {
    openPopup.mockRejectedValue({ code: 'auth/popup-blocked' });
    await expect(service.signInWithGoogle()).resolves.toBe('popup-blocked');
  });

  it('rethrows any other sign-in error', async () => {
    const error = { code: 'auth/network-request-failed' };
    openPopup.mockRejectedValue(error);
    await expect(service.signInWithGoogle()).rejects.toBe(error);
  });
});
