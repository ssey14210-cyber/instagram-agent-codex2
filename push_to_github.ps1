# Helper script to publish instagram-agent-codex to GitHub
param(
    [ValidateSet("public", "private")]
    [string]$Visibility = "public"
)

$env:PATH = "C:\Program Files\GitHub CLI;C:\Users\rohit\AppData\Local\GitHubDesktop\app-3.6.7\resources\app\git\cmd;$env:PATH"

Write-Host "`n=== Uploading instagram-agent-codex to GitHub ===" -ForegroundColor Cyan

# Check if origin remote already exists
$hasOrigin = git remote | Where-Object { $_ -eq "origin" }

if (!$hasOrigin) {
    Write-Host "Logging in and creating repository ($Visibility)..." -ForegroundColor Yellow
    gh auth login --web -h github.com -p https
    gh repo create instagram-agent-codex "--$Visibility" --source=. --remote=origin --push
} else {
    Write-Host "Remote origin already configured. Pushing main branch..." -ForegroundColor Yellow
    git push -u origin main
}

Write-Host "`nDone! Repository is live on GitHub." -ForegroundColor Green
