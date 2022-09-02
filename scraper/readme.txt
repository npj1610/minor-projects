this program serves as an usage example for the module "npj6.scraper". it collects data from a webpage by using GET requests and XPaths to locate information. main file outputs songs by Ty Segall that are not in 4/4 time signature, along with their possible time signatures.

depends on lxml.html

the module is a work in progress, i intend to allow a more realistic user-like behaviour. current features are:

- json cache file with 1 hour refresh time
- cache autosave within "with" statements
- optional cookies
- optional waiting time before making a real GET request

DISCLAIMER: use this software at your own discretion, i've already earned a few bans while developing it