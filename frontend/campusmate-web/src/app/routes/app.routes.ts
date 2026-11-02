import { Routes } from '@angular/router';
import { LoginComponent } from '../features/auth/login/login.component';

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  {
    path: 'dashboard',
    loadComponent: () => import('../features/dashboard/pages/dashboard.page').then((m) => m.DashboardPage),
  },
  { path: '', redirectTo: 'login', pathMatch: 'full' },
];
