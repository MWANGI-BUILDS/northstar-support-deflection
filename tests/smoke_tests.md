QA Testing Log — Northstar Support Chatbot Prototype

Tested By: QA Testing Lead  
Date: August 13, 2026  
Goal: Verify that the customer service chatbot correctly answers order questions, handles product returns, checks stock levels, and routes complex issues to human support.

Core Flow Verification

1. Checking Shipped Orders
- What Was Tested: Asked the chatbot where an active, shipped order was by typing: "Where is my order NS-10234?"
- Why It Was Tested: To ensure customers can quickly find out if a package is on the way without needing a support agent.
- Expected Result: The chatbot should tell the customer the package has shipped, name the courier (UPS), provide a tracking number, and give an arrival date.
- Actual Result: The chatbot correctly showed all UPS tracking details and stated it would arrive on Aug 13.
- Status: PASSED

2. Checking Orders Still Being Prepared
- What Was Tested: Asked about an order that has not shipped yet: "Has order NS-10250 shipped yet?"
- Why It Was Tested: Customers get anxious when items do not ship right away, so the bot needs to clearly explain processing status.
- Expected Result: The bot should explain that the item is currently being prepared and give an estimated dispatch date.
- Actual Result: The bot stated the item was being prepared and provided an estimated ship date of Aug 15.
- Status: PASSED

3. Requesting an Eligible Product Return
- What Was Tested: Clicked through the return menu, selected Apparel, and chose Within 30 days.
- Why It Was Tested: Returns are a major source of support tickets; automated approvals save time for both the store and the customer.
- Expected Result: The chatbot should confirm the return is allowed, explain how refund payments work, and send a shipping label.
- Actual Result: The bot confirmed eligibility, explained that refunds take 5–7 business days, and offered a prepaid label.
- Status: PASSED

4. Searching for a Non-Existent Order
- What Was Tested: Entered a fake order number: "Where is order NS-99999?"
- Why It Was Tested: To check how the bot handles typos or missing records gracefully instead of crashing.
- Expected Result: The chatbot should politely explain that the order was not found and offer to connect the customer with a real person.
- Actual Result: The chatbot stated it could not find the order and offered a "Talk to a human" button.
- Status: PASSED

5. Handling Unclear or Generic Messages
- What Was Tested: Typed a vague statement: "I need help"
- Why It Was Tested: Customers often type short phrases instead of choosing options, so the bot must guide them back on track.
- Expected Result: The chatbot should present the main menu choices (Order Status, Returns, Stock) so the user can pick what is needed.
- Actual Result: The bot asked the user to pick a topic and displayed all main menu buttons.
- Status: PASSED
Edge Case & Boundary Verification

6. Entering Order Numbers Without Prefixes
- What Was Tested: Typed the digits of an order number without the "NS-" prefix: 10234
- Why It Was Tested: Customers frequently type just numbers without formatting them properly.
- Expected Result: The bot should recognize the 5-digit number and look up order NS-10234.
- Actual Result: The regex parser converted bare digits to NS-10234 and retrieved the tracking status.
- Status: PASSED (Fix verified in latest build)

7. Reporting Damaged or Broken Items
- What Was Tested: Typed: "My package arrived damaged"
- Why It Was Tested: Broken goods require human attention and should not be handled by automated Q&A scripts.
- Expected Result: The chatbot should apologize immediately and connect the user to a human customer service agent.
- Actual Result: The chatbot expressed regret, recognized it as a priority damage claim, and automatically opened ticket #deflect-escalated.
- Status: PASSED

8. Asking About Stock in Different Sizes and Colors
- What Was Tested: Typed: "IS THE aurora sneaker IN STOCK IN SIZE s???" (using messy capitalization and extra question marks).
- Why It Was Tested: Real users do not type perfectly; the bot must understand messy text.
- Expected Result: The bot should clean up the text, recognize the product name and size "S", and report exact inventory counts.
- Actual Result: The chatbot ignored the punctuation and capital letters, confirming that 2 pairs of Aurora Sneakers in size S were available.
- Status: PASSED
