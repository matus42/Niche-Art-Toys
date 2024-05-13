# **Table Of Contents**

* [**Validator Testing**](#validator-testing)
  * [**HTML**](#html)
  * [**CSS**](#css)
  * [**Javascript**](#javascript)
  * [**Python**](#python)
* [**WAVE Evaluation Tool**](#wave-evaluation-tool)
* [**Lighthouse Reports**](#lighthouse-reports)
* [**Manual Testing**](#manual-testing)
  * [**Epics**](#epics)
  * [**User Stories**](#user-stories)
  * [**Error Testing**](#error-testing)
* [**Automated Testing**](#automated-testing)


## Validator Testing
### HTML
- All pages tested through direct input.
- i have few problems with double id's.
- Given the issue's complexity and my current time constraints, I plan to tackle this more thoroughly in the next update.

- Shopping Bag

![Shopping Bag](documentation/testing/bag_html.png)

- Add Product

![Add Product](documentation/testing/addproduct_html.png)

- Edit Product

![Edit Product](documentation/testing/editproduct_html.png)

- All others came out with no error.
- Home Page

![Home Page](documentation/testing/home_html.png)

- Main Product Page

![Main Page](documentation/testing/main_html.png)

- Product Detail

![Product Detail Page](documentation/testing/detail_html.png)

- Checkout

![Checkout Page](documentation/testing/checkout_html.png)


### CSS
- All css checkt via direct input
- Checkout css

![Checkout css](documentation/testing/checkout_css.png)

- Base css - 4 warnings

![Base css](documentation/testing/base_css.png)

![Warnings css](documentation/testing/warning_css.png)

- Profiles css

![Profiles css](documentation/testing/profiles_css.png)

- Contact css

![Contact css](documentation/testing/profiles_css.png)


### Javscript
- Tested my js through JSHint 

![js](documentation/testing/js1.png)

![js](documentation/testing/js2.png)

![js](documentation/testing/js3.png)

![js](documentation/testing/js4.png)

![js](documentation/testing/js5.png)

- Stripe js

![Stripe js](documentation/testing/stripe_js.png)


### Python
- I checked all Python files with Flake8 locally and the CI Python linter. Both indicated that only system files have errors, which we shouldn't alter. All other files passed without any issues.

- Bag view

![Bag View](documentation/testing/bag_views.png)

- Checkout view

![Checkout View](documentation/testing/checkout_view.png)

- Contact Us view

![Contact Us View](documentation/testing/contact_view.png)

- Profiles view

![Profiles View](documentation/testing/profile_views.png)