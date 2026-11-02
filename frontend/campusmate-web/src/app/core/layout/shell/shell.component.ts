import { Component, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';
import { Router, RouterOutlet } from '@angular/router';

import { AuthService } from '../../auth/auth.service';

/** Toolbar and page area shown on every signed-in screen. */
@Component({
  selector: 'app-shell',
  imports: [RouterOutlet, MatToolbarModule, MatButtonModule, MatIconModule],
  templateUrl: './shell.component.html',
  styleUrl: './shell.component.css',
})
export class ShellComponent {
  private readonly authService = inject(AuthService);
  private readonly router = inject(Router);

  async logout(): Promise<void> {
    await this.authService.signOut();
    await this.router.navigate(['/login'], { replaceUrl: true });
  }
}
