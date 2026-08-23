# Programming Learning Strategy & Roadmap

## 1. The Mindset: Rethinking "Dead Ends"
*   **Embrace the Detour:** There are no true dead ends in computer science. Wrestling with bugs builds problem-solving muscles. Logic transfers across all technologies.
*   **Syntax vs. Logic:** Advanced reasoning is the ability to systematically break massive, ambiguous problems into small, executable, logical steps, rather than just memorizing syntax.

## 2. Optimizing the Daily Routine (The 30-Day Python Challenge)
Currently on Day 11+. Stick to a 1-hour timebox with this 3-step loop:

1.  **Solve the Day's Problem (20–30 min):** Get the expected output working.
2.  **The "Two-Pass" Challenge (15–20 min):**
    *   Rewrite the solution using an alternative approach (e.g., `for` loop -> list comprehension).
    *   Intentionally break the code (change data types, remove conditions) to understand the exact errors Python throws (`TypeError`, `KeyError`, etc.).
3.  **The Strict AI Recall Rule (If stuck for 30+ minutes):**
    *   Read and understand the AI's explanation.
    *   **Close the AI window.**
    *   Write the code from pure recall. If you get stuck, you've pinpointed the exact logical gap.

## 3. Accountability System Adjustments
*   **Do NOT Skip Topics:** Skipping foundational concepts as a "penalty" for missing a day guarantees future failure. Programming is a staircase, not a buffet.
*   **Shift the Timeline:** If you miss a day, the next calendar day becomes the next sequential day of the challenge. The penalty is simply that the 30-day challenge takes 31+ calendar days to complete.
*   **Track Continuity:** Use a visual red 'X' on a calendar to mark a missed day as motivation, but pick up the curriculum exactly where you left off.
*   **Keep the Rest Day:** 1 rest day a week is mandatory for offline mental processing and preventing burnout.

## 4. Escaping Tutorial Hell
*   **The +1 Feature Rule:** Take an existing tutorial project (like a Flask/SQLAlchemy REST API) and add *one* new feature completely unassisted. This forces you to read documentation and design logic.

## 5. Future Project Roadmap: The Metadata Scrubber (Post-Day 30)
*Targeting the OSINT/Metadata curiosity without falling down a cybersecurity rabbit hole. Limit strictly to `.jpg` or `.png` files.*

*   **Phase 1: The Core Engine (CLI)**
    *   Build a pure Python script using `Pillow` and `piexif`.
    *   Input: Local file path. Output: Cleaned file saved locally.
    *   Goal: Strip EXIF data (e.g., GPS coordinates, camera model) without losing image quality.
*   **Phase 2: The API Wrapper (Flask)**
    *   Turn the CLI engine into a RESTful API route.
    *   Accept an image via a `POST` request (test in Postman).
    *   Process the image in memory and return the scrubbed file directly as the response. No databases.
*   **Phase 3: The Front-End (Optional)**
    *   Build a simple HTML page with an upload button.
    *   Connect it to the Flask API for browser-based scrubbing.
