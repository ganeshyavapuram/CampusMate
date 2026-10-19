import { Component, inject, OnInit, signal } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { RouterOutlet } from '@angular/router';

import { ApiService } from './core/http/api.service';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, MatButtonModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  private readonly api = inject(ApiService);

  protected readonly backendStatus = signal('checking…');

  ngOnInit(): void {
    this.api.health().subscribe({
      next: (res) => this.backendStatus.set(res.status),
      error: () => this.backendStatus.set('unreachable'),
    });
  }
}
