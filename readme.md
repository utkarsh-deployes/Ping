# Ping 

I built **Ping** because I was tired of manually checking job boards every single day. It is my very first automation project, designed to be a "set it and forget it" assistant that handles the job hunt for me while I sleep.

The logic is simple: every day, a scheduler automatically wakes up and fetches the latest job openings for my specific roles using an API. Instead of me having to go look for them, Ping "pings" my inbox with a fresh list of opportunities. At the same time, it saves all those jobs into a `.csv` file so I have a running history of every opening found. The best part is that it requires zero manual commands once it's set up, it just works.

---

## What It Does

* **The Hunt:** It connects to a job API to find new roles based on the titles I’ve chosen.
* **The Delivery:** It sends a daily email digest directly to my inbox so I can see updates over coffee.
* **The Archive:** It logs every single job into a local `.csv` file for future reference or tracking.
* **The Schedule:** It runs automatically every 24 hours without me ever having to touch the keyboard.

---

## Contributing
Since this is my first automation, I’m always looking to make it better. If you have an idea for a new feature or you found a bug that needs fixing, feel free to open an issue or submit a pull request!