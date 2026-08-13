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
