// Production settings. The live API address is filled in during deployment (DEP-01).
export const environment = {
  apiBaseUrl: '/api/v1',
  firebase: {
    apiKey: 'AIzaSyB3y2W1K56ozAB0xxnG7OY1NXb3PN3iOjM',
    authDomain: 'campusmate-f6440.firebaseapp.com',
    projectId: 'campusmate-f6440',
    storageBucket: 'campusmate-f6440.firebasestorage.app',
    messagingSenderId: '16773205003',
    appId: '1:16773205003:web:762c6b3c71833376be0b0e',
    measurementId: 'G-46QLT99BJ8',
  },
};

export const firebaseConfig = environment.firebase;
