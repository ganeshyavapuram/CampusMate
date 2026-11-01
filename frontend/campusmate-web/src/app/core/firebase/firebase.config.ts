import { initializeApp, getApps, getApp, FirebaseApp } from 'firebase/app';
import { getAnalytics, isSupported, Analytics } from 'firebase/analytics';
import { getAuth, Auth } from 'firebase/auth';
import { environment } from '../../../environments/environment';

export const firebaseConfig = environment.firebase;

// Initialize Firebase App (reuse existing instance if already initialized)
export const app: FirebaseApp =
  getApps().length === 0 ? initializeApp(firebaseConfig) : getApp();

// Auth instance for Google sign-in (AUTH-03)
export const auth: Auth = getAuth(app);

// Analytics instance (safely initialized in browser environments)
let analyticsInstance: Analytics | null = null;
if (typeof window !== 'undefined') {
  isSupported().then((supported) => {
    if (supported) {
      analyticsInstance = getAnalytics(app);
    }
  });
}

export const analytics = analyticsInstance;
