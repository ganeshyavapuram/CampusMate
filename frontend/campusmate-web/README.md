# CampusMate front end

Angular 21 app with Angular Material, laid out as described in [docs/folder-structure.md](../../docs/folder-structure.md) (ADR-031).

## First-time setup

You need Node.js 20.19+, 22.12+ or 24+ (`node --version`).

```bash
cd frontend/campusmate-web
npm install
```

## Run

The back end must be running too (see [backend/README.md](../../backend/README.md)).

```bash
npx ng serve
```

Open <http://localhost:4200>. The page should say **Back end status: ok**. The page reloads by itself when you save a file.

## Where the API address comes from

| File | Used by | API address |
|---|---|---|
| `src/environments/environment.development.ts` | `ng serve` | `http://127.0.0.1:8001/api/v1` |
| `src/environments/environment.ts` | `ng build` (production) | `/api/v1`, set at deployment (DEP-01) |

If your back end runs on another port, change `apiBaseUrl` in `environment.development.ts`.

## Tests

```bash
npx ng test --watch=false
```

Tests use Vitest and fake the back end with `HttpTestingController`, so the back end doesn't need to be running.

## Build

```bash
npx ng build
```

The output goes to `dist/campusmate-web/`.

## Folder layout

```
src/app/
├── app.ts, app.html, app.config.ts   # root component and app-wide providers
├── routes/app.routes.ts              # top-level routes; each feature is lazy-loaded
├── core/                             # app-wide singletons, loaded once
│   └── http/api.service.ts           # base URL and the health check
├── shared/                           # reusable pieces that know nothing about any feature
└── features/<feature>/               # one folder per feature: pages, components, services, models
```

Rules (ADR-031):

1. Features don't import other features.
2. `core/` and `shared/` never import from `features/`.
3. If two features need the same thing, move it to `shared/`.

## Adding something

```bash
npx ng generate component features/subjects/pages/subjects-list
npx ng generate service features/subjects/services/subjects
```

## Troubleshooting

| Problem | Fix |
|---|---|
| **Back end status: unreachable** | Start the back end, or make `apiBaseUrl` match its port. |
| `The Angular CLI requires a minimum Node.js version` | Update Node.js to a version listed above. |
| A Material component shows up unstyled | Import its module (for example `MatButtonModule`) in the component's `imports`. |
| `Port 4200 is already in use` | Stop the other `ng serve`, or run `npx ng serve --port 4300`. |
