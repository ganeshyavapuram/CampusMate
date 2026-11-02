import { Component, inject, signal } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { Router } from '@angular/router';

import { AuthService } from '../../../core/auth/auth.service';

@Component({
  selector: 'app-login',
  imports: [MatCardModule, MatButtonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
})
export class LoginComponent {
  private readonly authService = inject(AuthService);
  private readonly router = inject(Router);

  protected readonly signingIn = signal(false);
  protected readonly message = signal<string | null>(null);

  async signIn(): Promise<void> {
    this.signingIn.set(true);
    this.message.set(null);
    try {
      const result = await this.authService.signInWithGoogle();
      if (result === 'signed-in') {
        await this.router.navigate(['/dashboard']);
      } else if (result === 'popup-blocked') {
        this.message.set('Your browser blocked the Google sign-in window. Allow pop-ups for this site and try again.');
      } else {
        this.message.set('Sign-in was cancelled.');
      }
    } catch {
      this.message.set('Sign-in failed. Please try again.');
    } finally {
      this.signingIn.set(false);
    }
  }
}
