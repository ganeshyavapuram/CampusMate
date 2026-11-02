import { Injectable } from '@angular/core';
import { GoogleAuthProvider, UserCredential, signInWithPopup, signOut } from 'firebase/auth';

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

  /**
   * Whether a student is signed in. Waits for Firebase to restore the saved session first,
   * so a page refresh doesn't look like a signed-out visit.
   */
  async isSignedIn(): Promise<boolean> {
    await auth.authStateReady();
    return auth.currentUser !== null;
  }

  /** The signed-in student's Firebase ID token, or null when signed out. Firebase refreshes it when it expires. */
  async getIdToken(): Promise<string | null> {
    await auth.authStateReady();
    return auth.currentUser ? auth.currentUser.getIdToken() : null;
  }

  signOut(): Promise<void> {
    return signOut(auth);
  }

  protected openGooglePopup(): Promise<UserCredential> {
    return signInWithPopup(auth, new GoogleAuthProvider());
  }
}
