Scenario :: Product Search

TEST CASE1:Search with valid product data.

TEST DATA: Snowboard

TEST STEPS:
Open https://adnabu-store-assignment1.myshopify.com in chrome browser.
Login with your credetials
In Product Search enter 'Snowboard'
Click search icon.

EXPECTED RESULTS:
adnabu store should show all products of Snowboard.


TEST CASE2:Search with partial product data.

TEST DATA: snow

TEST STEPS:
Open https://adnabu-store-assignment1.myshopify.com in chrome browser.
Login with your credetials
In Product Search enter 'snow'
Click search icon.

EXPECTED RESULTS:
adnabu store should show all snow related products.


TEST CASE3:Search with special charecters(complex-long strings).

TEST DATA: @#$!@#$ttyt

TEST STEPS:
Open https://adnabu-store-assignment1.myshopify.com in chrome browser.
Login with your credetials
In Product Search enter '@#$!@#$ttyt'
Click search icon.

EXPECTED RESULTS:
adnabu store should give error message of "No results found for “@#$!@#$ttyt”. Check the spelling or use a different word or phrase"

TEST CASE4:Search with without passing any data.

TEST DATA: No-data

TEST STEPS:
Open https://adnabu-store-assignment1.myshopify.com in chrome browser.
Login with your credetials
In Product Search ,enter nothing 
Click search icon.

EXPECTED RESULTS:
adnabu store shows nothing and can be active only after mouse click to access store web page.

Scenario :: Add cart

TEST CASE5:Add item to cart,check the cart,click check out button

TEST DATA: The Collection Snowboard: Liquid

TEST STEPS:
Open https://adnabu-store-assignment1.myshopify.com in chrome browser.
Login with your credetials
In Product Search ,enter "The Collection Snowboard: Liquid"
Click search icon.
After item displayd ,click on Add to cart button.
Click on check out button

EXPECTED RESULTS:
Your cart  should up with correct price ,no of items correctly.
Subtotal must be same as price of the item.
Customer must be able to click on check out button and it directs to payment page as per business document/HLD.

TEST CASE6:Check Add cart button appears for sold out products.

TEST DATA: Football - 2023 - Panini Illusions Football - Hobby Box (10 Packs)

TEST STEPS:
Open https://adnabu-store-assignment1.myshopify.com in chrome browser.
Login with your credetials
In Product Search ,enter "Football - 2023 - Panini Illusions Football - Hobby Box (10 Packs)"
Click search icon.
After item displayd ,check add cart button appears.

EXPECTED RESULTS:
Add cart should not appear for sold out products.

TEST CASE7:Check Add cart shows correct sum of money for the increased and decreased no of items.

TEST DATA: snow
          The Videographer Snowboard  

TEST STEPS:
Open https://adnabu-store-assignment1.myshopify.com in chrome browser.
Login with your credetials
In Product Search ,enter "snow"
Click search icon.
After item related to snow displayed ,click on "The Videographer Snowboard "
Click on Add to cart 5 ti,es ,so we can add 5 items.
After Your cart appears, try to increase no of items by clicking on '+'
Now reduce no of items to 1 by clicking on '-'
Try to remove item from your cart further.

EXPECTED RESULTS:
User able to click on Add to cart .
Your cart displays the item with ,5 item and it's respective price.
Usercan increase no of items by clicking on '+' and it's respective sub total money appears correctly..
User can  reduce no. of items to 1 and its respective sub total appears.
User cant reduce no of items further  or remove item from your cart and '-' button must disable.
