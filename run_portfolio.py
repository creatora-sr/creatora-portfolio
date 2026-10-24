import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

# HTML Content with ALL Detailed Sections, Images, Links and LOGO.PNG
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CREATORA S.R | Where Ideas Become Creation</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brandDark: '#0B0F19',
                        brandCard: '#111827',
                        neonCyan: '#00f2fe',
                        neonPink: '#4facfe',
                        neonPurple: '#7000ff'
                    }
                }
            }
        }
    </script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .glow-text {
            text-shadow: 0 0 15px rgba(0, 242, 254, 0.6);
        }
        .glow-box {
            box-shadow: 0 0 25px rgba(112, 0, 255, 0.25);
        }
        .glow-box:hover {
            box-shadow: 0 0 35px rgba(0, 242, 254, 0.4);
        }
        .glass-card {
            background: rgba(17, 24, 39, 0.75);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        html { background: #0B0F19; }
        body { background: transparent; }
        #bgCanvas {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: -1;
            pointer-events: none;
        }
        .spark {
            position: fixed;
            width: 7px; height: 7px;
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            background: radial-gradient(circle, #ffffff, #00f2fe 40%, #7000ff);
            box-shadow: 0 0 10px #00f2fe, 0 0 20px #7000ff;
            animation: sparkFly 0.7s ease-out forwards;
        }
        @keyframes sparkFly {
            0% { transform: translate(0,0) scale(1); opacity: 1; }
            100% { transform: translate(var(--dx), var(--dy)) scale(0); opacity: 0; }
        }

        .brand-float {
            position: absolute;
            bottom: 8px;
            right: 12px;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 0.25em;
            color: rgba(255,255,255,0.06);
            pointer-events: none;
            z-index: 0;
            animation: brandFloat 6s ease-in-out infinite;
            text-transform: uppercase;
        }
        @keyframes brandFloat {
            0%,100% { transform: translateY(0); opacity: 0.05; }
            50% { transform: translateY(-8px); opacity: 0.12; }
        }
    </style>
</head>
<body class="text-gray-100 font-sans antialiased selection:bg-cyan-500 selection:text-black">
    <canvas id="bgCanvas"></canvas>

    <!-- NAVBAR -->
    <nav class="fixed top-0 left-0 w-full z-50 glass-card border-b border-gray-800 px-6 py-4">
        <div class="max-w-7xl mx-auto flex justify-between items-center">
            <!-- Brand Logo -->
            <a href="#" class="flex items-center gap-3 group">
                <img src="LOGO.png" alt="CREATORA S.R Logo" class="w-10 h-10 rounded-full object-cover border border-cyan-400/50 shadow-md">
                <div>
                    <span class="text-xl font-extrabold tracking-wider bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-500">
                        CREATORA S.R
                    </span>
                    <p class="text-[10px] text-gray-400 font-medium tracking-widest uppercase">Where Ideas Become Creation</p>
                </div>
            </a>

            <!-- Nav Links -->
            <div class="hidden md:flex items-center gap-8 font-medium text-sm text-gray-300">
                <a href="#about" class="hover:text-cyan-400 transition">About Me</a>
                <a href="#expertise" class="hover:text-cyan-400 transition">Expertise</a>
                <a href="#portfolio" class="hover:text-cyan-400 transition">Client Work</a>
                <a href="#pricing" class="hover:text-cyan-400 transition">Pricing Plans</a>
                <a href="#contact" class="px-5 py-2 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-semibold shadow-lg hover:opacity-90 transition">
                    Contact Us
                </a>
            </div>
        </div>
    </nav>

    <!-- HERO SECTION -->
    <section class="pt-36 pb-20 px-6 relative overflow-hidden">
        <div class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[500px] h-[500px] bg-purple-600/20 rounded-full blur-[120px] pointer-events-none"></div>
        <div class="max-w-5xl mx-auto text-center relative z-10">
            <!-- Hero Header Logo Badge -->
            <div class="flex justify-center mb-6">
                <img src="LOGO.png" alt="CREATORA S.R Logo" class="w-24 h-24 rounded-full border-2 border-cyan-400 p-1 bg-gray-900 shadow-2xl shadow-cyan-500/20">
            </div>
            <span class="inline-block px-4 py-1.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 mb-6">
                🚀 AI-POWERED DIGITAL SOLUTIONS AGENCY
            </span>
            <h1 class="text-4xl md:text-6xl font-black tracking-tight leading-tight mb-6">
                Your ideas our creation = <br>
                <span class="bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-500 glow-text">
                    Powerful Digital Solutions
                </span>
            </h1>
            <p class="text-lg md:text-xl text-gray-400 max-w-3xl mx-auto mb-10 leading-relaxed">
                Welcome to <strong class="text-white">CREATORA S.R</strong> ("Where Ideas Become Creation"). We combine cutting-edge Artificial Intelligence with modern design to scale your brand online.
            </p>
            <div class="flex flex-wrap justify-center gap-4">
                <a href="#portfolio" class="px-8 py-3.5 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-bold shadow-lg hover:shadow-cyan-500/25 transition">
                    Explore Our Client Work
                </a>
                <a href="https://wa.me/917015804907?text=Hello%20Sneha,%20I%20want%20to%20discuss%20a%20project" target="_blank" class="px-8 py-3.5 rounded-full glass-card text-white font-semibold hover:border-cyan-400 transition flex items-center gap-2">
                    <i class="fab font-bold fa-whatsapp text-emerald-400 text-lg"></i> Direct WhatsApp
                </a>
            </div>
        </div>
    </section>

    <!-- DETAILED ABOUT ME SECTION -->
    <section id="about" class="py-20 px-6 bg-slate-950/50">
        <div class="max-w-6xl mx-auto">
            <div class="grid md:grid-cols-12 gap-12 items-center">
                
                <!-- Founder Logo Card -->
                <div class="md:col-span-5 flex justify-center">
                    <div class="relative group w-full max-w-sm">
                        <div class="absolute -inset-1 bg-gradient-to-r from-cyan-500 to-purple-600 rounded-3xl blur opacity-75 group-hover:opacity-100 transition duration-500"></div>
                        <div class="relative glass-card p-8 rounded-3xl text-center border border-gray-700">
                            <img src="LOGO.png" alt="Sneha Rani - CREATORA S.R Logo" class="w-32 h-32 mx-auto mb-6 rounded-full border-2 border-cyan-400 p-1 bg-gray-900 object-cover shadow-xl">
                            <h3 class="text-2xl font-bold text-white mb-1">Sneha Rani</h3>
                            <p class="text-cyan-400 font-medium text-sm mb-4">Founder & Lead Digital Strategist</p>
                            <div class="p-3 rounded-xl bg-gray-900/80 border border-gray-800 text-xs text-gray-300">
                                "Detail-oriented execution designed to drive online growth and maximum brand visibility."
                            </div>
                        </div>
                    </div>
                </div>

                <!-- About Details Text -->
                <div class="md:col-span-7">
                    <span class="text-cyan-400 font-bold tracking-widest text-xs uppercase mb-2 block">ABOUT CREATORA S.R</span>
                    <h2 class="text-3xl md:text-4xl font-extrabold text-white mb-6 leading-tight">
                        Welcome to CREATORA S.R, <span class="text-cyan-400">"Where Ideas Become Creation."</span>
                    </h2>
                    <p class="text-gray-300 leading-relaxed mb-4">
                        I am <strong>Sneha Rani</strong>, the founder of <strong>CREATORA S.R</strong>, and I deliver powerful digital solutions for businesses and creators by combining cutting-edge Artificial Intelligence with modern design.
                    </p>
                    <p class="text-gray-400 leading-relaxed mb-8">
                        My approach is highly detail-oriented, ensuring that every single project is handled with precision, top-tier quality, and strategic execution designed to drive online growth and maximum brand visibility.
                    </p>

                    <!-- Core Mission -->
                    <div class="p-6 rounded-2xl glass-card border-l-4 border-cyan-400">
                        <h4 class="text-white font-bold text-base mb-2 flex items-center gap-2">
                            <i class="fas fa-bullseye text-cyan-400"></i> My Core Mission
                        </h4>
                        <p class="text-sm text-gray-300 leading-relaxed">
                            To convert your vision into a successful digital identity with <strong>100% client satisfaction</strong>, <strong>on-time delivery</strong>, and <strong>innovative creative ideas</strong> in every project.
                        </p>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- CORE EXPERTISE & DETAILED SERVICES -->
    <section id="expertise" class="py-20 px-6">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-16">
                <span class="text-cyan-400 font-bold text-xs uppercase tracking-widest">OUR CAPABILITIES</span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-white mt-2">Core Expertise & Detailed Services</h2>
            </div>

            <div class="grid md:grid-cols-2 gap-8">
                
                <!-- 1. Custom AI Agents & Automation -->
                <div class="glass-card p-8 rounded-3xl border border-gray-800 hover:border-cyan-500/50 transition">
                    <div class="w-12 h-12 rounded-2xl bg-cyan-500/10 text-cyan-400 flex items-center justify-center text-xl mb-6">
                        <i class="fas fa-robot"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-4">1. Custom AI Agents & Automation</h3>
                    <ul class="space-y-3 text-sm text-gray-300">
                        <li class="flex items-start gap-2">
                            <i class="fas fa-check-circle text-cyan-400 mt-1"></i>
                            Developing smart AI agents to streamline business workflows and handle repetitive tasks.
                        </li>
                        <li class="flex items-start gap-2">
                            <i class="fas fa-check-circle text-cyan-400 mt-1"></i>
                            Setting up intelligent automation systems for query handling, lead management, and time-saving efficiency.
                        </li>
                    </ul>
                </div>

                <!-- 2. Web Designing & Development -->
                <div class="glass-card p-8 rounded-3xl border border-gray-800 hover:border-purple-500/50 transition">
                    <div class="w-12 h-12 rounded-2xl bg-purple-500/10 text-purple-400 flex items-center justify-center text-xl mb-6">
                        <i class="fas fa-code"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-4">2. Web Designing & Development</h3>
                    <ul class="space-y-3 text-sm text-gray-300">
                        <li class="flex items-start gap-2">
                            <i class="fas fa-check-circle text-purple-400 mt-1"></i>
                            Designing modern, fully responsive, and user-friendly websites that look flawless on all devices.
                        </li>
                        <li class="flex items-start gap-2">
                            <i class="fas fa-check-circle text-purple-400 mt-1"></i>
                            Writing clean, SEO-friendly code to ensure better search visibility and higher reach.
                        </li>
                        <li class="flex items-start gap-2">
                            <i class="fas fa-check-circle text-purple-400 mt-1"></i>
                            Ensuring fast-loading, secure, and smooth overall performance.
                        </li>
                    </ul>
                </div>

                <!-- 3. AI Video & Content Creation -->
                <div class="glass-card p-8 rounded-3xl border border-gray-800 hover:border-pink-500/50 transition">
                    <div class="w-12 h-12 rounded-2xl bg-pink-500/10 text-pink-400 flex items-center justify-center text-xl mb-6">
                        <i class="fas fa-video"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-4">3. AI Video & Content Creation</h3>
                    <ul class="space-y-3 text-sm text-gray-300">
                        <li class="flex items-start gap-2">
                            <i class="fas fa-check-circle text-pink-400 mt-1"></i>
                            Creating stunning, engaging videos powered by artificial intelligence.
                        </li>
                        <li class="flex items-start gap-2">
                            <i class="fas fa-check-circle text-pink-400 mt-1"></i>
                            Producing captivating posts, reels, carousels, blogs, and captions tailored to connect with your target audience.
                        </li>
                        <li class="flex items-start gap-2">
                            <i class="fas fa-check-circle text-pink-400 mt-1"></i>
                            Providing professional video editing for advertisements, YouTube, and reels.
                        </li>
                    </ul>
                </div>

                <!-- 4. Graphics & Visual Branding -->
                <div class="glass-card p-8 rounded-3xl border border-gray-800 hover:border-amber-500/50 transition">
                    <div class="w-12 h-12 rounded-2xl bg-amber-500/10 text-amber-400 flex items-center justify-center text-xl mb-6">
                        <i class="fas fa-palette"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-4">4. Graphics & Visual Branding</h3>
                    <ul class="space-y-3 text-sm text-gray-300">
                        <li class="flex items-start gap-2">
                            <i class="fas fa-check-circle text-amber-400 mt-1"></i>
                            Designing custom logos, flyers, social media creatives, and eye-catching promotional posters for brand awareness.
                        </li>
                        <li class="flex items-start gap-2">
                            <i class="fas fa-check-circle text-amber-400 mt-1"></i>
                            Creating high-converting YouTube thumbnails and attractive banners designed to boost clicks and views.
                        </li>
                    </ul>
                </div>

            </div>
        </div>
    </section>

    <!-- CLIENT PROJECTS PORTFOLIO SECTION (WITH IMAGES & LIVE LINKS) -->
    <section id="portfolio" class="py-20 px-6 bg-slate-950/50">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-16">
                <span class="text-cyan-400 font-bold text-xs uppercase tracking-widest">PROVEN RESULTS</span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-white mt-2">Our Featured Client Projects</h2>
                <p class="text-gray-400 text-sm mt-2">Click any project to visit the live website directly</p>
            </div>

            <div class="grid md:grid-cols-2 gap-8">
                
                <!-- Project 1: Divya Computers -->
                <a href="https://divya-computer-m27.github.io/divya-computers/" target="_blank" class="group glass-card rounded-3xl overflow-hidden border border-gray-800 hover:border-cyan-400 transition flex flex-col justify-between">
                    <div>
                        <div class="h-52 relative overflow-hidden">
                            <img src="divya.png" alt="Divya Computers Preview" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-gray-900 via-gray-900/40 to-transparent"></div>
                            <span class="absolute top-4 left-4 px-3 py-1 rounded-full text-xs font-semibold bg-cyan-500/80 text-black">Tech & Computer Repair</span>
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold text-white group-hover:text-cyan-400 transition">Divya Computers</h3>
                            <p class="text-xs text-gray-300 mt-2">Complete laptop repair, screen replacement, motherboard diagnostics, and OS software installation platform.</p>
                        </div>
                    </div>
                    <div class="px-6 py-4 bg-gray-900/80 border-t border-gray-800 flex justify-between items-center">
                        <span class="text-xs text-gray-400">divya-computer-m27.github.io</span>
                        <span class="text-cyan-400 text-xs font-bold flex items-center gap-1 group-hover:translate-x-1 transition">
                            Visit Live Site <i class="fas fa-external-link-alt"></i>
                        </span>
                    </div>
                </a>

                <!-- Project 2: SmartBiz AI -->
                <a href="https://smartbiz-ai-d3aca.web.app/" target="_blank" class="group glass-card rounded-3xl overflow-hidden border border-gray-800 hover:border-purple-400 transition flex flex-col justify-between">
                    <div>
                        <div class="h-52 relative overflow-hidden">
                            <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80" alt="SmartBiz AI Preview" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-gray-900 via-gray-900/40 to-transparent"></div>
                            <span class="absolute top-4 left-4 px-3 py-1 rounded-full text-xs font-semibold bg-purple-500/80 text-white">AI Automation App</span>
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold text-white group-hover:text-purple-400 transition">SmartBiz AI</h3>
                            <p class="text-xs text-gray-300 mt-2">AI-driven business automation web app for lead management, smart chatbots, and automated workflows.</p>
                        </div>
                    </div>
                    <div class="px-6 py-4 bg-gray-900/80 border-t border-gray-800 flex justify-between items-center">
                        <span class="text-xs text-gray-400">smartbiz-ai-d3aca.web.app</span>
                        <span class="text-purple-400 text-xs font-bold flex items-center gap-1 group-hover:translate-x-1 transition">
                            Visit Live Site <i class="fas fa-external-link-alt"></i>
                        </span>
                    </div>
                </a>

                <!-- Project 3: Srishti Real Estate -->
                <a href="https://srishti-real-estate.web.app/" target="_blank" class="group glass-card rounded-3xl overflow-hidden border border-gray-800 hover:border-emerald-400 transition flex flex-col justify-between">
                    <div>
                        <div class="h-52 relative overflow-hidden">
                            <img src="https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=800&q=80" alt="Srishti Real Estate Preview" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-gray-900 via-gray-900/40 to-transparent"></div>
                            <span class="absolute top-4 left-4 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/80 text-black">Real Estate Portal</span>
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold text-white group-hover:text-emerald-400 transition">Srishti Real Estate</h3>
                            <p class="text-xs text-gray-300 mt-2">Modern property portal featuring high-end property listings, interactive filter searches, and direct buyer inquiries.</p>
                        </div>
                    </div>
                    <div class="px-6 py-4 bg-gray-900/80 border-t border-gray-800 flex justify-between items-center">
                        <span class="text-xs text-gray-400">srishti-real-estate.web.app</span>
                        <span class="text-emerald-400 text-xs font-bold flex items-center gap-1 group-hover:translate-x-1 transition">
                            Visit Live Site <i class="fas fa-external-link-alt"></i>
                        </span>
                    </div>
                </a>

                <!-- Project 4: Artist World S.R -->
                <a href="https://artistworldsr2027-max.github.io/" target="_blank" class="group glass-card rounded-3xl overflow-hidden border border-gray-800 hover:border-pink-400 transition flex flex-col justify-between">
                    <div>
                        <div class="h-52 relative overflow-hidden">
                            <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=800&q=80" alt="Artist World S.R Preview" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-gray-900 via-gray-900/40 to-transparent"></div>
                            <span class="absolute top-4 left-4 px-3 py-1 rounded-full text-xs font-semibold bg-pink-500/80 text-white">EdTech & YouTube</span>
                        </div>
                        <div class="p-6">
                            <h3 class="text-2xl font-bold text-white group-hover:text-pink-400 transition">Artist World S.R</h3>
                            <p class="text-xs text-gray-300 mt-2">Educational learning platform & content hub offering online art tutorials, practice sessions ,offline workshop and YouTube video integration.</p>
                        </div>
                    </div>
                    <div class="px-6 py-4 bg-gray-900/80 border-t border-gray-800 flex justify-between items-center">
                        <span class="text-xs text-gray-400">artistworldsr2027-max.github.io</span>
                        <span class="text-pink-400 text-xs font-bold flex items-center gap-1 group-hover:translate-x-1 transition">
                            Visit Live Site <i class="fas fa-external-link-alt"></i>
                        </span>
                    </div>
                </a>

            </div>
        </div>
    </section>

    <!-- PRICING PACKAGES SECTION -->
    <section id="pricing" class="py-20 px-6">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-12">
                <span class="text-cyan-400 font-bold text-xs uppercase tracking-widest">TRANSPARENT PRICING</span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-white mt-2">Flexible Packages For Every Business</h2>
                <p class="text-gray-400 text-sm mt-2">Choose between monthly flexible plans or save up to 20% on yearly plans.</p>
            </div>

            <!-- Pricing Toggle Switch -->
            <div class="flex justify-center items-center gap-4 mb-16">
                <span id="monthlyLabel" class="text-sm font-bold text-cyan-400">Monthly</span>
                <button id="pricingToggle" onclick="togglePricing()" class="w-14 h-8 bg-gray-800 rounded-full p-1 border border-gray-700 relative transition">
                    <div id="toggleDot" class="w-6 h-6 bg-cyan-400 rounded-full transition-all transform translate-x-0"></div>
                </button>
                <span id="yearlyLabel" class="text-sm font-medium text-gray-400 flex items-center gap-2">
                    Yearly Package <span class="px-2 py-0.5 rounded-full text-[10px] bg-emerald-500/20 text-emerald-400 font-bold">SAVE 20%</span>
                </span>
            </div>

            <!-- Pricing Cards Grid -->
            <div class="grid md:grid-cols-3 gap-8">
                
                <!-- Starter Package -->
                <div class="glass-card p-8 rounded-3xl border border-gray-800 relative flex flex-col justify-between">
                    <div>
                        <h3 class="text-xl font-bold text-white mb-2">Starter</h3>
                        <p class="text-xs text-gray-400 mb-6">Perfect for Creators & Small Businesses</p>
                        <div class="text-3xl font-black text-white mb-6">
                            <span id="starterPrice">₹5,999</span>
                            <span id="starterPeriod" class="text-xs font-normal text-gray-400">/month</span>
                        </div>
                        <ul class="space-y-3 text-sm text-gray-300 mb-8">
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> 1 AI Agent Setup</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> AI Video & Graphic Design</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> Web & Banner Design</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> Basic Revisions & Support</li>
                        </ul>
                    </div>
                    <a href="https://wa.me/917015804907?text=Hi%20Sneha,%20I%20am%20interested%20in%20Starter%20Package" target="_blank" class="w-full py-3 rounded-xl bg-gray-800 text-cyan-400 font-bold text-center hover:bg-cyan-500 hover:text-black transition">
                        Select Plan
                    </a>
                </div>

                <!-- Growth Package (Most Popular) -->
                <div class="glass-card p-8 rounded-3xl border-2 border-cyan-400 relative flex flex-col justify-between glow-box">
                    <div class="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-extrabold text-xs tracking-wider uppercase">
                        Most Popular
                    </div>
                    <div>
                        <h3 class="text-xl font-bold text-white mb-2">Growth</h3>
                        <p class="text-xs text-gray-400 mb-6">More Reach, Engagement & Sales</p>
                        <div class="text-3xl font-black text-white mb-6">
                            <span id="growthPrice">₹9,999</span>
                            <span id="growthPeriod" class="text-xs font-normal text-gray-400">/month</span>
                        </div>
                        <ul class="space-y-3 text-sm text-gray-300 mb-8">
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> Up to 3 AI Agents</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> Advanced AI Video Creation</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> SEO Web Design & Graphics</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> Priority Client Support</li>
                        </ul>
                    </div>
                    <a href="https://wa.me/917015804907?text=Hi%20Sneha,%20I%20am%20interested%20in%20Growth%20Package" target="_blank" class="w-full py-3 rounded-xl bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-bold text-center shadow-lg hover:opacity-90 transition">
                        Select Plan
                    </a>
                </div>

                <!-- Premium Package -->
                <div class="glass-card p-8 rounded-3xl border border-gray-800 relative flex flex-col justify-between">
                    <div>
                        <h3 class="text-xl font-bold text-white mb-2">Premium</h3>
                        <p class="text-xs text-gray-400 mb-6">Full Creative Power & All-in-One</p>
                        <div class="text-3xl font-black text-white mb-6">
                            <span id="premiumPrice">₹17,999</span>
                            <span id="premiumPeriod" class="text-xs font-normal text-gray-400">/month</span>
                        </div>
                        <ul class="space-y-3 text-sm text-gray-300 mb-8">
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> Up to 5 Custom AI Agents</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> Full Video, Content & Graphic Suite</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> Complete Custom Website Setup</li>
                            <li class="flex items-center gap-2"><i class="fas fa-check text-cyan-400"></i> Dedicated Support & Revisions</li>
                        </ul>
                    </div>
                    <a href="https://wa.me/917015804907?text=Hi%20Sneha,%20I%20am%20interested%20in%20Premium%20Package" target="_blank" class="w-full py-3 rounded-xl bg-gray-800 text-cyan-400 font-bold text-center hover:bg-cyan-500 hover:text-black transition">
                        Select Plan
                    </a>
                </div>

            </div>
        </div>
    </section>

    <!-- CONTACT SECTION -->
    <section id="contact" class="py-20 px-6 bg-slate-950/50">
        <div class="max-w-4xl mx-auto glass-card p-10 rounded-3xl border border-gray-800 text-center">
            <h2 class="text-3xl font-extrabold text-white mb-4">Let's Build Something Great Together!</h2>
            <p class="text-gray-400 text-sm mb-8">
                Reach out to Sneha Rani for custom inquiries, project consultation, or AI automation setup.
            </p>

            <div class="grid md:grid-cols-3 gap-6 mb-10 text-left">
                <div class="p-4 rounded-2xl bg-gray-900/60 border border-gray-800">
                    <i class="fas fa-phone-alt text-cyan-400 mb-2"></i>
                    <p class="text-xs text-gray-400">Phone / WhatsApp</p>
                    <p class="text-sm font-bold text-white">+91 7015804907</p>
                </div>
                <div class="p-4 rounded-2xl bg-gray-900/60 border border-gray-800">
                    <i class="fas fa-envelope text-cyan-400 mb-2"></i>
                    <p class="text-xs text-gray-400">Email Address</p>
                    <p class="text-sm font-bold text-white">creatoras.r27@gmail.com</p>
                </div>
                <div class="p-4 rounded-2xl bg-gray-900/60 border border-gray-800">
                    <i class="fas fa-map-marker-alt text-cyan-400 mb-2"></i>
                    <p class="text-xs text-gray-400">Office Location</p>
                    <p class="text-sm font-bold text-white">Hisar, Haryana, India</p>
                </div>
            </div>

            <a href="https://wa.me/917015804907?text=Hello%20Sneha,%20I%20have%20a%20project%20query" target="_blank" class="px-8 py-3.5 rounded-full bg-emerald-500 text-black font-bold flex items-center gap-2 mx-auto w-fit hover:bg-emerald-400 transition">
                <i class="fab fa-whatsapp text-lg"></i> Chat Directly On WhatsApp
            </a>
        </div>
    </section>


    <!-- JUST FOR FUN: MINI RUNNER GAME -->
    <section id="minigame" class="py-20 px-6 bg-slate-950/50">
        <div class="max-w-6xl mx-auto text-center">
            <span class="text-cyan-400 font-bold text-xs uppercase tracking-widest">JUST FOR FUN</span>
            <h2 class="text-3xl md:text-4xl font-extrabold text-white mt-2 mb-2">Mini Runner</h2>
            <p class="text-gray-400 text-sm mb-6">Press Space / Tap / Click to jump. Avoid obstacles, collect coins!</p>
            <div class="relative mx-auto" style="max-width:800px;">
                <canvas id="gameCanvas" width="800" height="300" class="w-full rounded-2xl border border-gray-800 bg-gray-900 cursor-pointer"></canvas>
                <div id="gameOverlay" class="absolute inset-0 flex flex-col items-center justify-center bg-black/70 rounded-2xl">
                    <p class="text-white text-xl font-bold mb-4">Ready to run?</p>
                    <button id="gameStartBtn" class="px-6 py-3 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-bold shadow-lg hover:opacity-90 transition">Start Game</button>
                </div>
            </div>
            <div class="mt-4 flex justify-center gap-6 text-sm">
                <span class="text-gray-300">Score: <strong id="gameScore" class="text-cyan-400">0</strong></span>
                <span class="text-gray-300">Best: <strong id="gameBest" class="text-purple-400">0</strong></span>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="py-8 border-t border-gray-800 text-center text-xs text-gray-500">
        <div class="flex justify-center items-center gap-2 mb-3">
            <img src="LOGO.png" alt="CREATORA S.R Logo" class="w-6 h-6 rounded-full object-cover">
            <span class="font-bold text-gray-300">CREATORA S.R</span>
        </div>
        <p>© 2026 CREATORA S.R — Where Ideas Become Creation. All rights reserved.</p>
        <p class="mt-1">Founded by Sneha Rani | Hisar, Haryana</p>
    </footer>

    <!-- JavaScript For Interactive Pricing Toggle -->
    <script>
        let isYearly = false;
        function togglePricing() {
            isYearly = !isYearly;
            const toggleDot = document.getElementById('toggleDot');
            const monthlyLabel = document.getElementById('monthlyLabel');
            const yearlyLabel = document.getElementById('yearlyLabel');

            const starterPrice = document.getElementById('starterPrice');
            const growthPrice = document.getElementById('growthPrice');
            const premiumPrice = document.getElementById('premiumPrice');

            const starterPeriod = document.getElementById('starterPeriod');
            const growthPeriod = document.getElementById('growthPeriod');
            const premiumPeriod = document.getElementById('premiumPeriod');

            if (isYearly) {
                toggleDot.classList.add('translate-x-6');
                monthlyLabel.classList.remove('text-cyan-400');
                monthlyLabel.classList.add('text-gray-400');
                yearlyLabel.classList.add('text-cyan-400');

                starterPrice.innerText = "₹39,999";
                growthPrice.innerText = "₹79,999";
                premiumPrice.innerText = "₹1,49,999";

                starterPeriod.innerText = "/year";
                growthPeriod.innerText = "/year";
                premiumPeriod.innerText = "/year";
            } else {
                toggleDot.classList.remove('translate-x-6');
                yearlyLabel.classList.remove('text-cyan-400');
                yearlyLabel.classList.add('text-gray-400');
                monthlyLabel.classList.add('text-cyan-400');

                starterPrice.innerText = "₹5,999";
                growthPrice.innerText = "₹9,999";
                premiumPrice.innerText = "₹17,999";

                starterPeriod.innerText = "/month";
                growthPeriod.innerText = "/month";
                premiumPeriod.innerText = "/month";
            }
        }
    </script>

    <!-- Background Animation + Cursor Spark -->
    <script>
        const canvas = document.getElementById('bgCanvas');
        const ctx = canvas.getContext('2d');
        let particles = [];
        let brandTexts = [];
        let t = 0;
        let mouse = { x: -9999, y: -9999 };
        window.addEventListener('mousemove', (e) => { mouse.x = e.clientX; mouse.y = e.clientY; });
        window.addEventListener('mouseleave', () => { mouse.x = -9999; mouse.y = -9999; });
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        function initParticles() {
            particles = [];
            const count = Math.min(60, Math.floor(window.innerWidth * window.innerHeight / 18000));
            for (let i = 0; i < count; i++) {
                particles.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    r: Math.random() * 1.8 + 0.4,
                    vx: (Math.random() - 0.5) * 0.4,
                    vy: (Math.random() - 0.5) * 0.4,
                    alpha: Math.random() * 0.5 + 0.2,
                    hue: Math.random() > 0.5 ? 185 : 275
                });
            }
            brandTexts = [];
            const bcount = 4;
            for (let i = 0; i < bcount; i++) {
                brandTexts.push({
                    x: Math.random() * (canvas.width - 160) + 80,
                    y: Math.random() * (canvas.height - 60) + 40,
                    vx: (Math.random() - 0.5) * 0.7 + (Math.random() > 0.5 ? 0.35 : -0.35),
                    vy: (Math.random() - 0.5) * 0.7 + (Math.random() > 0.5 ? 0.3 : -0.3),
                    size: 15 + Math.random() * 12,
                    alpha: 0.06 + Math.random() * 0.06,
                    rot: (Math.random() - 0.5) * 0.4,
                    vrot: (Math.random() - 0.5) * 0.0015,
                    phase: Math.random() * Math.PI * 2,
                    hue: Math.random() > 0.5 ? 190 : 275
                });
            }
        }
        initParticles();
        window.addEventListener('resize', initParticles);

        function drawBg() {
            t += 0.005;
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // animated mesh gradient base
            const g = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
            g.addColorStop(0, `hsla(260, 60%, 8%, 1)`);
            g.addColorStop(0.5, `hsla(220, 50%, 6%, 1)`);
            g.addColorStop(1, `hsla(200, 60%, 8%, 1)`);
            ctx.fillStyle = g;
            ctx.fillRect(0,0,canvas.width,canvas.height);

            // moving colorful orbs
            const orbs = [
                {x: 0.25 + 0.15*Math.sin(t*0.7), y: 0.3 + 0.1*Math.cos(t*0.9), c: '112,0,255', r: 0.35},
                {x: 0.75 + 0.12*Math.cos(t*0.8), y: 0.7 + 0.12*Math.sin(t*1.1), c: '0,242,254', r: 0.32},
                {x: 0.5 + 0.2*Math.sin(t*0.5), y: 0.5 + 0.18*Math.cos(t*0.6), c: '79,172,254', r: 0.28},
            ];
            orbs.forEach(o => {
                const gg = ctx.createRadialGradient(o.x*canvas.width, o.y*canvas.height, 0, o.x*canvas.width, o.y*canvas.height, o.r*canvas.width);
                gg.addColorStop(0, `rgba(${o.c},0.14)`);
                gg.addColorStop(1, `rgba(${o.c},0)`);
                ctx.fillStyle = gg;
                ctx.fillRect(0,0,canvas.width,canvas.height);
            });

            // connecting lines between nearby particles
            for (let i = 0; i < particles.length; i++) {
                for (let j = i+1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.hypot(dx,dy);
                    if (dist < 95) {
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.strokeStyle = `rgba(0,242,254,${0.08*(1-dist/110)})`;
                        ctx.lineWidth = 0.6;
                        ctx.stroke();
                    }
                }
            }

            // particles
            particles.forEach(p => {
                // gentle attraction toward cursor
                const dx = mouse.x - p.x;
                const dy = mouse.y - p.y;
                const d = Math.hypot(dx, dy);
                if (d > 0 && d < 180) {
                    p.vx += (dx / d) * 0.008;
                    p.vy += (dy / d) * 0.008;
                }
                // damping
                p.vx *= 0.985;
                p.vy *= 0.985;
                // keep min speed
                if (Math.hypot(p.vx, p.vy) < 0.05) { p.vx += (Math.random()-0.5)*0.02; p.vy += (Math.random()-0.5)*0.02; }
                p.x += p.vx;
                p.y += p.vy;
                if (p.x < 0) p.x = canvas.width;
                if (p.x > canvas.width) p.x = 0;
                if (p.y < 0) p.y = canvas.height;
                if (p.y > canvas.height) p.y = 0;
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
                ctx.fillStyle = `hsla(${p.hue}, 100%, 72%, ${p.alpha})`;
                ctx.fill();
            });

            // game-like bouncing CREATORA S.R words
            brandTexts.forEach(b => {
                b.x += b.vx;
                b.y += b.vy;
                b.rot += b.vrot;
                // measure text width approx
                const tw = b.size * 9.2;
                if (b.x <= 0) { b.x = 0; b.vx = Math.abs(b.vx); }
                if (b.x + tw >= canvas.width) { b.x = canvas.width - tw; b.vx = -Math.abs(b.vx); }
                if (b.y - b.size <= 0) { b.y = b.size; b.vy = Math.abs(b.vy); }
                if (b.y >= canvas.height) { b.y = canvas.height; b.vy = -Math.abs(b.vy); }
                const pulse = 0.85 + 0.15*Math.sin(t*3 + b.phase);
                const a = b.alpha * pulse;
                ctx.save();
                ctx.translate(b.x, b.y);
                ctx.rotate(b.rot);
                ctx.font = `900 ${b.size}px sans-serif`;
                ctx.shadowColor = `hsla(${b.hue},100%,60%,0.9)`;
                ctx.shadowBlur = 10;
                // gradient fill
                const gg = ctx.createLinearGradient(0, -b.size, tw, b.size);
                gg.addColorStop(0, `hsla(${b.hue},100%,75%,${a})`);
                gg.addColorStop(1, `hsla(${b.hue+40},100%,65%,${a})`);
                ctx.fillStyle = gg;
                ctx.fillText('CREATORA S.R', 0, 0);
                ctx.restore();
            });

            requestAnimationFrame(drawBg);
        }
        drawBg();

        // Cursor spark animation (enhanced)
        let lastSpark = 0;
        document.addEventListener('mousemove', (e) => {
            const now = Date.now();
            if (now - lastSpark < 12) return;
            lastSpark = now;
            const count = 3;
            for (let i = 0; i < count; i++) {
                const spark = document.createElement('div');
                spark.className = 'spark';
                const ox = (Math.random() - 0.5) * 10;
                const oy = (Math.random() - 0.5) * 10;
                spark.style.left = (e.clientX + ox) + 'px';
                spark.style.top = (e.clientY + oy) + 'px';
                const angle = Math.random() * Math.PI * 2;
                const dist = Math.random() * 44 + 10;
                spark.style.setProperty('--dx', (Math.cos(angle) * dist) + 'px');
                spark.style.setProperty('--dy', (Math.sin(angle) * dist) + 'px');
                document.body.appendChild(spark);
                setTimeout(() => spark.remove(), 750);
            }
        });

        // Floating brand watermark in each section
        document.querySelectorAll('section').forEach((sec, i) => {
            const w = document.createElement('div');
            w.className = 'brand-float';
            w.textContent = 'CREATORA S.R';
            w.style.animationDelay = (i * 0.7) + 's';
            sec.style.position = sec.style.position || 'relative';
            sec.appendChild(w);
        });
    </script>

    <!-- Mini Runner Game -->
    <script>
        (function() {
            const canvas = document.getElementById('gameCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const logoImg = new Image();
            logoImg.src = 'LOGO.png';
            const W = canvas.width, H = canvas.height;
            const groundY = H - 40;
            let player, obstacles, coins, score, best, speed, running, raf, spawnTimer, coinTimer;
            best = parseInt(localStorage.getItem('runnerBest') || '0', 10) || 0;
            document.getElementById('gameBest').textContent = best;

            function reset() {
                player = { x: 80, y: groundY, w: 32, h: 40, vy: 0, jumping: false, frame: 0 };
                obstacles = [];
                coins = [];
                score = 0;
                speed = 5;
                spawnTimer = 0;
                coinTimer = 0;
                running = true;
                document.getElementById('gameScore').textContent = '0';
                document.getElementById('gameOverlay').style.display = 'none';
            }

            function jump() {
                if (!running) return;
                if (!player.jumping) {
                    player.vy = -13;
                    player.jumping = true;
                }
            }

            function spawnObstacle() {
                const tall = Math.random() < 0.35;
                const h = tall ? 55 + Math.random()*20 : 28 + Math.random()*18;
                const w = tall ? 26 : 20 + Math.random()*16;
                obstacles.push({ x: W + 20, y: groundY - h + (tall?0: (player.h - h)), w, h, tall });
            }
            function spawnCoin() {
                const y = groundY - 60 - Math.random()*80;
                coins.push({ x: W + 20, y, r: 8, collected: false });
            }

            function update() {
                if (!running) return;
                // player physics
                player.vy += 0.6;
                player.y += player.vy;
                if (player.y >= groundY) {
                    player.y = groundY;
                    player.vy = 0;
                    player.jumping = false;
                }
                player.frame++;

                // speed ramp
                speed = 5 + score / 400;
                if (speed > 12) speed = 12;

                // spawn obstacles
                spawnTimer++;
                if (spawnTimer > (90 - Math.min(40, score/10))) {
                    spawnTimer = 0;
                    spawnObstacle();
                }
                coinTimer++;
                if (coinTimer > 110) {
                    coinTimer = 0;
                    spawnCoin();
                }

                // move obstacles
                obstacles.forEach(o => o.x -= speed);
                obstacles = obstacles.filter(o => o.x + o.w > -20);

                // move coins
                coins.forEach(c => c.x -= speed);
                coins = coins.filter(c => c.x + c.r > -20 && !c.collected);

                // coin collection
                coins.forEach(c => {
                    if (!c.collected) {
                        const dx = (player.x + player.w/2) - c.x;
                        const dy = (player.y - player.h/2) - c.y;
                        if (Math.hypot(dx,dy) < c.r + 18) {
                            c.collected = true;
                            score += 50;
                            document.getElementById('gameScore').textContent = score;
                        }
                    }
                });

                // collisions
                for (const o of obstacles) {
                    const px = player.x, py = player.y - player.h;
                    const pw = player.w, ph = player.h;
                    if (px < o.x + o.w && px + pw > o.x && py < o.y + o.h && py + ph > o.y) {
                        gameOver();
                        return;
                    }
                }

                score += 1;
                document.getElementById('gameScore').textContent = score;
            }

            function gameOver() {
                running = false;
                if (score > best) {
                    best = score;
                    localStorage.setItem('runnerBest', best);
                    document.getElementById('gameBest').textContent = best;
                }
                const ov = document.getElementById('gameOverlay');
                ov.style.display = 'flex';
                ov.innerHTML = '<p class="text-white text-xl font-bold mb-2">Game Over!</p><p class="text-gray-300 text-sm mb-4">Score: ' + score + '</p><button id="gameRestartBtn" class="px-6 py-3 rounded-full bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-bold shadow-lg hover:opacity-90 transition">Play Again</button>';
                document.getElementById('gameRestartBtn').addEventListener('click', startGame);
            }

            function draw() {
                ctx.clearRect(0,0,W,H);
                // sky gradient
                const g = ctx.createLinearGradient(0,0,0,H);
                g.addColorStop(0, '#0B0F19');
                g.addColorStop(1, '#111827');
                ctx.fillStyle = g;
                ctx.fillRect(0,0,W,H);

                // ground
                ctx.fillStyle = '#1f2937';
                ctx.fillRect(0, groundY, W, H - groundY);
                ctx.fillStyle = '#00f2fe';
                ctx.fillRect(0, groundY, W, 2);

                // moving ground stripes
                const stripeOffset = (player.frame * speed) % 40;
                ctx.fillStyle = 'rgba(0,242,254,0.15)';
                for (let i = -1; i < W/40 + 1; i++) {
                    ctx.fillRect(i*40 - stripeOffset, groundY + 12, 20, 3);
                }

                // obstacles
                obstacles.forEach(o => {
                    ctx.fillStyle = o.tall ? '#7000ff' : '#4facfe';
                    ctx.shadowColor = o.tall ? '#7000ff' : '#4facfe';
                    ctx.shadowBlur = 10;
                    ctx.fillRect(o.x, o.y, o.w, o.h);
                    ctx.shadowBlur = 0;
                });

                // coins
                coins.forEach(c => {
                    if (c.collected) return;
                    ctx.beginPath();
                    ctx.arc(c.x, c.y, c.r, 0, Math.PI*2);
                    ctx.fillStyle = '#fbbf24';
                    ctx.shadowColor = '#fbbf24';
                    ctx.shadowBlur = 12;
                    ctx.fill();
                    ctx.shadowBlur = 0;
                });

                // player (logo)
                ctx.shadowColor = '#00f2fe';
                ctx.shadowBlur = 15;
                if (logoImg.complete && logoImg.naturalWidth > 0) {
                    ctx.drawImage(logoImg, player.x, player.y - player.h, player.w, player.h);
                } else {
                    ctx.fillStyle = '#00f2fe';
                    ctx.fillRect(player.x, player.y - player.h, player.w, player.h);
                }
                ctx.shadowBlur = 0;
            }

            function loop() {
                update();
                draw();
                if (running) raf = requestAnimationFrame(loop);
            }

            function startGame() {
                reset();
                loop();
            }
            window.startGame = startGame;

            document.getElementById('gameStartBtn').addEventListener('click', startGame);
            canvas.addEventListener('click', jump);
            window.addEventListener('keydown', (e) => {
                if (e.code === 'Space' || e.code === 'ArrowUp') {
                    e.preventDefault();
                    jump();
                }
            });
            // touch
            canvas.addEventListener('touchstart', (e) => { e.preventDefault(); jump(); });

            // initial draw
            reset();
            running = false;
            draw();
            document.getElementById('gameOverlay').style.display = 'flex';
        })();
    </script>

</body>
</html>
"""

def generate_and_serve():
    file_name = "index.html"
    port = 8000

    # 1. Write HTML Content to index.html
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"✅ Successfully updated '{file_name}' with full details, project images and LOGO.PNG.")

    # 2. Start HTTP Server and open browser
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    url = f"http://localhost:{port}"

    print(f"🚀 Server running at: {url}")
    webbrowser.open(url)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")
        sys.exit()

if __name__ == "__main__":
    generate_and_serve()