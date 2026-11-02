import { Routes } from '@angular/router';
import { authGuard } from '../core/auth/auth.guard';
import { ShellComponent } from '../core/layout/shell/shell.component';
import { LoginComponent } from '../features/auth/login/login.component';

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  // Every signed-in page goes under the shell, so the guard and the Logout toolbar cover it.
  {
    path: '',
    component: ShellComponent,
    canActivate: [authGuard],
    children: [
      {
        path: 'dashboard',
        loadComponent: () => import('../features/dashboard/pages/dashboard.page').then((m) => m.DashboardPage),
      },
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
    ],
  },
  { path: '**', redirectTo: '' },
];
