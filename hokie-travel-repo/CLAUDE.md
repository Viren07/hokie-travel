# Hokie Travel — Project Context

This file gives Claude (and any teammate) the full context for the **Hokie Travel** clickable prototype. It covers the idea, the decisions made so far, and how the code is organized. Read it before changing anything.

## 1. The project

- **Course:** Virginia Tech Honors Studio, Team 1, "Getting There"
- **Team:** Will Collins (documenter, trust map), Viren Agarwal (evidence from social media, tab icons), Samriddhi Baranwal (facilitator, planning, persona, prototyping), Breanna Brooks (evidence from official sites, systems/trust map, app tab structure), Maya Almeda
- **Studio prompt:** How might we make it easier for people to reach and participate in an essential everyday activity?
- **Our how-might-we:** How might we reduce transportation barriers for Virginia Tech students caused by unreliable bus access and limited parking availability?
- **Purpose statement:** A solution to VT transportation problems that gives students an easier, one-stop place to find transportation options. VT and Blacksburg already have Blacksburg Transit, RIDE Solutions (rideshare), Parking Services and bike permits, but they are separate, disconnected tools. That fragmentation is why students feel the existing options aren't enough. Putting them in one app targets the root of the problem.
- **Deliverable:** A prototype that shows what the app does. We are not building a working app. It may also become a pitch to VT Transportation / Parking Services.
- **Name and brand:** "Hokie Travel", with the line "made by a fellow Hokie". Name idea from Will. Logo: a bus with Hokie footprints circling it (Sam's idea), made in Canva. Tagline ideas are on hold: From dorm to door · Go anywhere Hokies · Flock together · Where will you go.

## 2. The problem, with evidence

**Bus (Blacksburg Transit, "BT")**
- 19 routes, 49 buses, about 19,700 riders per weekday (Q1 2026), about 5 million trips a year. VT students, faculty and staff are 95% of riders, and their fares are prepaid, so almost everyone funnels into one free system. It is a high-growth system that is outgrowing itself, not a neglected one.
- Overcrowding, skipped stops and inaccurate arrival times. BT's own service alerts admit that buses sometimes don't show on the map while still running, plus "technical difficulties" and battery recalls affecting 28 electric buses (Jan 2026).
- The third-party "HokieTransit" app shows only one bus option and can't plan ahead. Its crowding feature depends on how many people use the app, and too few do, so it's inaccurate. BT's trip planner makes you type exact street addresses, but students know building names.
- Off-campus waits can reach 30+ minutes. Winter and ice make it worse. Missing one bus can add an hour.
- An Uber for what should be a 5-minute drive costs $20–25. Reliable transport forces students to rent near campus, making that a necessity rather than a luxury.

**Parking**
- A permit is required 7 AM–10 PM, Monday–Friday, even when classes aren't in session. Restricted spaces are always enforced. Permits are now plate-based (virtual), and hourly parking in peripheral lots goes through ParkMobile.
- A permit costs about $600. Parking without one (for example at the Cassell lot) is a $40 ticket.
- Duck Pond and other lots are always full. Faculty-only and athlete-only lots (Perry, Cassell) often sit empty but still get ticketed. Team idea: let students reserve restricted spots by time slot instead of for a whole day.

**Existing alternatives and gaps**
- **RIDE Solutions:** free VT ride-matching with a Guaranteed Ride Home program, but it's built for work commutes, not same-day, spontaneous or social rides. There's also a VT Carpool Permit.
- **Zipcar on campus (older program):** a few cars at the Drillfield and Squires, about $7.50/hr or $69/day. Too small for demand.
- **Bike share:** Roam NRV (75 e-bikes across 16 stations) closed in June 2022. Blacksburg currently has no bike share.

**Persona "Bob":** Bob won't leave his apartment because getting around is too hard, so he misses club events. Professor Jeremy connected this to student loneliness, which widens who will care about the solution.

## 3. Feedback that shaped the scope

- **Professor Brad:** getting to and around campus and getting to the Cascades or Roanoke are two different problems. Narrow down, and back the argument with evidence (this is a problem because of X, and this solution addresses it because of Y).
- **AI feedback (Getting There doc):** keep the population broad (on- and off-campus students) but narrow the problem to **bus reliability plus parking availability**, with "campus mobility" as the umbrella. The core app idea is a tool that helps students decide *how* to get somewhere, for example "Dorm → Pamplin by 10:00: bus arriving 9:37 (high capacity), drive 8 min (parking nearby), carpool available, walk/bike 22 min."
- **Team decision (in this chat):** we still keep all five tabs from the Canva mockup, including Car Rental and the Cascades use case, and we **add Parking** on top.

## 4. App features (what the prototype shows)

| Area | Features |
|---|---|
| **Live bus directions** ● | **Real data.** Bus tab → Get Directions: type a start and destination (or 📍 my location), leave now / depart at / arrive by, best / less walking / fewer transfers. Shows every bus option like Google Maps (times, route chips, departure stop, walking, transfers, fare), step-by-step details, and draws the chosen route on a live map. The home map is also live, with BT routes drawn on it |
| **Bus** | Schedule, live tracking, capacity %, on-time %, rider reports (bus full / skipped stop / running late), backup plan if the bus is full, weather and map-glitch alerts |
| **Trip planner** | Search by **building name**, arrive-by time, "I have a car" switch, compare all options sorted by most reliable / fastest / cheapest, mixed trips (e.g. bike + walk), plan a trip ahead |
| **Carpool** | Match to a car, closest ride now, plan ahead, **recurring carpool groups**, drop-offs along the way. Riders pay a small fee (~$2); drivers get gas money plus rewards (30% off local restaurants, 50% off a dining-hall meal). Safety: verified VT students only, opt-in, live tracking, **no carpools 12–5 AM or on game days** |
| **Bike rental** | Nearest bike, scan QR to unlock, reserve ahead, $1 per 30 min, week / month / semester plans, hotspots with charging docks, GPS-tracked, bikes power down outside the service area |
| **Car rental** | Pick up on campus ("you don't need a car to get to your car"), filter by type (hybrid / sedan / SUV / van for move-in), rent by hour, day, week, month or semester, student discount, gas + insurance included |
| **Parking** | Filter by permit (commuter / resident / hourly), live open-spot counts, best lot right now, restricted-but-empty lots with the $40 ticket warning and a **time-slot request** |
| **Calendar auto-planner** ★ | Connect **Google Calendar, VT Outlook, Apple Calendar and Canvas**. **Fully automatic:** it books carpool seats and rental cars, holds bikes, sets leave-now alerts, and **re-plans on its own** when a bus fills up (with Undo). Settings: arrive-early buffer and switches for each automation. Viren says the Google Calendar integration is feasible to code |

## 5. The prototype code

```
hokie-travel/
├── CLAUDE.md                     ← this file
├── hokie-travel-prototype.html   ← BUILT file. Open it in any browser. Don't edit it by hand.
├── build.py                      ← embeds the images into the template → rebuilds the HTML + site/
├── make_qr.py                    ← QR code for the hosted site → qr-code.png
├── netlify.toml                  ← tells Netlify to publish site/
├── site/                         ← what gets hosted: index.html + apple-touch-icon.png
└── src/
    ├── template.html             ← EDIT THIS: all HTML, CSS and JS
    └── assets/                   ← images cut from the team's Canva mockup
        ├── logo.png  wordmark.png  loading-route.png  map.jpg
        └── nav-bus.png  nav-bike.png  nav-carpool.png  nav-rental.png  nav-cal.png
```

**Workflow:** edit `src/template.html`, run `python3 build.py`, then open `hokie-travel-prototype.html`. The template uses placeholders such as `{{LOGO}}`, `{{WORDMARK}}` and `{{NAV_BUS}}`, and `build.py` swaps each one for an embedded image. The built file is fully self-contained, so it can be emailed or put on a USB drive and works offline (only the Inter web font needs internet; without it the page falls back to a system font).

**How it works:**
- A single page with a 375×780 phone frame. Each screen is a `<section class="screen" id="s-NAME">`. `show("NAME")` switches screens, and `loadThen("NAME")` shows the loading animation first.
- Screen names: `splash, loading, home, transit, search, results, busdetail, bus, bike, carpool, rental, parking, plan`.
- Click wiring uses data attributes: `data-go="screen"`, `data-tab="screen"` (bottom nav), `data-back`, `data-toast="message"`, `data-modal` (QR scanner), `data-jump` (desktop side panel).
- **All sample data** is in arrays at the top of the `<script>`: `PLACES, BUSES, LOTS, POOLS, BIKES, CARS, CALS`. The calendar day plans are in `renderDay()` (Thu / Fri / Sat). Change the numbers there.
- The bottom nav has six buttons: the team's own icons for Rent Bike, Carpool, Car Rental and Calendar, the **Blacksburg Transit (BT) logo** for the Bus tab (`nav-bus.png`, white background removed so it sits on the grey bar; the team's original bus icon was replaced at Viren's request), plus a Parking icon drawn in the same black style, placed between Car Rental and Calendar. The Bus button opens the home map, and "Live buses" on the map opens the bus list. Parking can also be reached from the drive option in trip results.
- Colors are CSS variables in `:root`: maroon `#7b1c1c`, orange `#ff8a4c`, red `#ff3b30`, light card `#c8cfd9`, nav grey `#66696c`, black background.
- **Headers:** the "Hokie Travel" wordmark only appears on the splash and loading screens. The six main tabs (home map, bike, carpool, car rental, parking, calendar) have no wordmark header (class `tabscreen` gives them a top gap).
- **Light / dark mode:** the ☀/☾ button next to "Get Directions" on the home map (and "Theme" in the desktop side panel) switches themes. The choice is saved in the browser; with no saved choice it follows the device setting. Dark values live in `:root`, light values in `:root[data-theme="light"]`. When adding UI, use the variables (`--surface`, `--ink`, `--muted`, `--warm-*`, `--cool-*`, `--track`...) instead of hex colors, or it will look wrong in one of the themes. Splash and loading stay dark in both themes because they're built on the black-background Canva art.

**Live bus data (the `transit` screen and the home map):**
- Uses Google's **Routes API** (`directions/v2:computeRoutes`, `travelMode: TRANSIT`, bus only, alternatives on) and the **Maps JavaScript API** (map, route lines, `TransitLayer`). Google builds these from Blacksburg Transit's own schedule and real-time feed. HokieTransit has no public API.
- Needs a Google Maps API key with both APIs enabled. Either paste it in the app (🔑 button, saved in that browser only) or build it in: `GMAPS_KEY=AIza... python3 build.py`, or put it in `src/gmaps-key.txt`. Don't commit the key or publish/share a build that has it inside. Restrict the key to those two APIs in Google Cloud.
- Without a key, or where Google is blocked (the published claude.ai preview blocks outside requests), the home map falls back to the screenshot and the transit screen asks for a key. Open the built HTML file in a browser for the live version.
- What's still sample data: the Bus list / bus detail screens (capacity %, on-time %, rider reports) and the trip-planner comparison. Google doesn't provide crowding or live vehicle positions.
- Code: everything after the `LIVE BUS DIRECTIONS` comment at the bottom of the script. `searchTransit()` builds the request, `parseRoute()` turns Google's steps into walk/bus segments, `renderOptions()` draws the list, `drawRoute()` draws the map.

**Hosting + QR code:**
- **Live site: https://hokietravel.netlify.app/** (Netlify). Code lives in GitHub repo `Viren07/hokie-travel`.
- `python3 build.py` also writes `site/` (`index.html` + `apple-touch-icon.png`), the folder that gets hosted. `netlify.toml` tells Netlify to publish `site/`, so once Netlify is linked to the GitHub repo, every push redeploys automatically. Without the link, drag the `site` folder onto the site's Deploys page in Netlify.
- `qr-code.png` opens the Netlify site. `python3 make_qr.py <url>` makes a new one if the address changes.
- On phones (≤500px wide) the fake phone frame is dropped and the app fills the screen; "Add to Home Screen" gives it an app icon and hides the browser bar.
- Never upload a build with a Google key inside (build.py warns). Remove the Canva watermark from the logo before sharing publicly.

**Rules for editing:**
- **Do not redraw or restyle the logo, the "Hokie Travel" wordmark, the loading route graphic or the tab icons.** The BT logo is Blacksburg Transit's trademark; ask BT before using it in anything beyond the class prototype. They are exact crops from the team's Canva design. To change them, re-export from Canva and replace the file in `src/assets/` with the same name.
- The logo export has a faint **Canva watermark** over the bus. Re-export without it (Canva Pro, or a licensed element) before any final presentation.
- The home map is a screenshot of Google Maps from the mockup. It's fine for a class prototype, but replace it for anything public.
- All routes, times, lot counts, prices and names are **sample data**. Label them as such when presenting.

## 6. Demo path (for presenting)

1. Tap the splash logo → loading animation → home map ("Hi Bob, Take a ride").
2. Calendar tab → connect Google, Outlook and Canvas → **Plan my rides**.
3. Wait about 3 seconds: the "Re-planned automatically" banner appears because the bus is full and you've been moved to a carpool. Tap any ride to change it.
4. Open **Sat** to see the Cascades hike with a rental car and friends added.
5. Get Directions → Pamplin Hall → live bus options from Google → Steps → "Compare with carpool, bike & parking" → Bus → report "Bus full".
6. Tab through Bike, Carpool (see *My groups* and *Drive & earn*), Car Rental and Parking.

On a laptop, the side panel next to the phone has jump links to every screen.

## 7. Open items / next steps

- Survey results (Google Form posted to YikYak, group chats, dorm and club chats) → put the real numbers into the pitch and the prototype.
- Viren's idea: embed prototype screenshots in the survey and ask whether the features would help, confuse, or get used.
- Finish the trust/systems map (Breanna/Will), empathy maps, storyboard.
- Decide whether regional trips (Cascades, Claytor Lake, Radford, Roanoke) stay in the pitch or become "future scope", since both Professor Brad and the feedback flagged them as a separate problem.
- Optional: a physical version (cardboard or foam phone) if there's time.

## 8. Source links (from the team doc)

- Canva prototype: https://canva.link/rqcyxr21d4uitw8
- Team notes (Google Doc): https://docs.google.com/document/d/1yxWRjIII1KhP8_BmfxrQfz4KbRGPcWo3Ejth903n7_Q/edit
- BT: https://ridebt.org · https://www.ridebt.org/10-routes-and-schedules · https://getaround.vt.edu/getting-around-vt/blacksburg-transit.html
- Parking: https://parking.vt.edu/parking/students.html · https://parking.vt.edu/permits.html · https://news.vt.edu/notices/evpcoo/2026-27-Academic-Year-Permit-Sales-and-Reminders-for-Students.html
- Carpool: https://getaround.vt.edu/ride-share/carpool.html · https://ridesolutions.org/ride-solutions-location/new-river-valley/
- Zipcar at VT: https://news.vt.edu/articles/2013/09/090613-vpa-zipcar.html
- Student complaints: r/VirginiaTech parking thread, r/blacksburg BT threads, Instagram parking reel (links in the team doc)
