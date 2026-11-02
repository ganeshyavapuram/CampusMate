import { Component } from '@angular/core';

// Placeholder until the dashboard is built (Phase 4).
@Component({
  selector: 'app-dashboard-page',
  template: `
    <main class="dashboard">
      <h1>Dashboard</h1>
      <p>You're signed in. Your dashboard is coming soon.</p>
    </main>
  `,
  styles: `
    .dashboard {
      max-width: 960px;
      margin: 0 auto;
      padding: 2rem 1rem;
    }
  `,
})
export class DashboardPage {}
