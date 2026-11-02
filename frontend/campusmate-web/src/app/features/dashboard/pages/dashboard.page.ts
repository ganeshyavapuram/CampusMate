import { Component, OnInit, inject, signal } from '@angular/core';

import { ApiService } from '../../../core/http/api.service';

// Placeholder until the dashboard is built (Phase 4).
@Component({
  selector: 'app-dashboard-page',
  template: `
    <main class="dashboard">
      <h1>Dashboard</h1>
      <p>You're signed in. Your dashboard is coming soon.</p>
      <p class="status">Back end status: <strong data-testid="backend-status">{{ backendStatus() }}</strong></p>
    </main>
  `,
  styles: `
    .dashboard {
      max-width: 960px;
      margin: 0 auto;
      padding: 2rem 1rem;
    }

    .status {
      color: var(--mat-sys-on-surface-variant, #444);
    }
  `,
})
export class DashboardPage implements OnInit {
  private readonly api = inject(ApiService);

  protected readonly backendStatus = signal('checking…');

  ngOnInit(): void {
    this.api.health().subscribe({
      next: (res) => this.backendStatus.set(res.status),
      error: () => this.backendStatus.set('unreachable'),
    });
  }
}
