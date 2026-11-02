import { Injectable } from '@angular/core';
import { GoogleAuthProvider, UserCredential, signInWithPopup } from 'firebase/auth';

import { auth } from '../firebase/firebase.config';

export type SignInResult = 'signed-in' | 'cancelled' | 'popup-blocked';

// Firebase error codes thrown when the student closes or abandons the Google popup.
const CANCELLED_CODES = new Set([
  'auth/popup-closed-by-user',
  'auth/cancelled-popup-request',
  'auth/user-cancelled',
]);

/** Google sign-in through Firebase Authentication (ADR-004). */
@Injectable({ providedIn: 'root' })
export class AuthService {
  /**
   * Opens the Google popup. Resolves 'cancelled' if the student closes it and 'popup-blocked'
   * if the browser stops it opening; rethrows any other error.
   */
  async signInWithGoogle(): Promise<SignInResult> {
    try {
      await this.openGooglePopup();
      return 'signed-in';
    } catch (err) {
      const code = (err as { code?: string })?.code ?? '';
      if (CANCELLED_CODES.has(code)) {
        return 'cancelled';
      }
      if (code === 'auth/popup-blocked') {
        return 'popup-blocked';
      }
      throw err;
    }
  }

  protected openGooglePopup(): Promise<UserCredential> {
    return signInWithPopup(auth, new GoogleAuthProvider());
  }
}
