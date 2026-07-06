from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MyMoney - Personal Finance Tracker</title>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
        <style>
            :root {
                --primary: #10b981;
                --primary-dark: #059669;
                --bg: #0f172a;
                --card-bg: #1e293b;
                --text: #f8fafc;
                --text-muted: #94a3b8;
            }
            body {
                margin: 0;
                font-family: 'Outfit', sans-serif;
                background-color: var(--bg);
                color: var(--text);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                overflow: hidden;
            }
            .container {
                text-align: center;
                padding: 2rem;
                background: rgba(30, 41, 59, 0.7);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 24px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.3);
                max-width: 500px;
                width: 90%;
                animation: fadeIn 1s ease-out;
            }
            h1 {
                font-size: 3rem;
                font-weight: 800;
                margin-bottom: 0.5rem;
                background: linear-gradient(135deg, #34d399, #059669);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            p {
                color: var(--text-muted);
                font-size: 1.1rem;
                line-height: 1.6;
                margin-bottom: 2rem;
            }
            .badge {
                display: inline-block;
                background: rgba(16, 185, 129, 0.15);
                color: var(--primary);
                padding: 0.5rem 1rem;
                border-radius: 9999px;
                font-weight: 600;
                font-size: 0.875rem;
                margin-bottom: 1.5rem;
                border: 1px solid rgba(16, 185, 129, 0.2);
            }
            .btn {
                display: inline-block;
                background: var(--primary);
                color: #ffffff;
                text-decoration: none;
                padding: 0.75rem 2rem;
                border-radius: 12px;
                font-weight: 600;
                transition: all 0.3s ease;
                box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
            }
            .btn:hover {
                background: var(--primary-dark);
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(16, 185, 129, 0.6);
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <span class="badge">Vercel Deployment Ready</span>
            <h1>MyMoney</h1>
            <p>Welcome to your personal finance dashboard. Your Django project is now successfully running on Vercel!</p>
            <a href="/admin/" class="btn">Go to Admin Portal</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

