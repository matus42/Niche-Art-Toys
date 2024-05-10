# Welcome to Niche Art & Toys!
Niche Art & Toys is an independently owned bussiness offering a carefully curated selection of handcrafted toys, watercolor paintings, and modern calligraphy pieces. Our platform caters to art lovers, collectors, and those seeking the perfect, heartfelt gift.

# **Table Of Contents**

* [**Planning Phase**](#planning-phase)
  * [**Strategy**](#strategy)
    * [**Service Aims:**](#service-aims)
    * [**Opportunities:**](#opportunities)
  * [**Scope**](#scope)
  * [**Structure**](#structure)
    * [**User Stories:**](#user-stories)
  * [**Skeleton**](#skeleton)
    * [**Wireframes:**](#wireframes)
    * [**User Flow Diagram:**](#user-flow-diagram)
    * [**Database Schema**](#database-schema)
  * [**Surface**](#surface)
    * [**Color Schema:**](#color-scheme)
    * [**Typography:**](#typography)
* [**E-commerce Application Type**](#e-commerce-application-type)
* [**Marketing Strategies**](#marketing-strategies)  
* [**SEO considerations**](#seo-considerations)
* [**Agile Development Process**](#agile-development-process)

* [**Features**](#features)
  
* [**User Experience (UX)**](#user-experience-ux)

  * [**Design Philosophy**](#design-philosophy)

* [**Technologies Used**](#technologies-used)

  * [**Front-End Technologies:**](#front-end-technologies)
  * [**Back-End Technologies:**](#back-end-technologies)

* [**Testing Phase**](#testing-phase)

* [**Deployment**](#deployment)

* [**Future Development**](#future-development)

* [**Credits**](#credits)
  * [**Acknowledgements:**](#acknowledgements)


# Planning Phase

## Strategy
### Service Aims
Our service aims focus on delivering exceptional value to our customers through:

1. **Quality and Craftsmanship**: Ensuring every product meets high standards of quality and uniqueness.
2. **Customer Experience**: Providing a seamless and satisfying shopping experience from browsing to checkout.
3. **Sustainability**: Committing to eco-friendly practices in production and packaging to minimize our environmental impact.
4. **Community Engagement**: Creating a vibrant community of artists and art lovers through interactive events and social media engagement.
5. **Innovation**: Continuously improving and innovating our product offerings and user interface based on customer feedback and market trends.

### Opportunities:
The current market and technological landscape present several opportunities for Niche Art & Toys:

1. **Growing Interest in Handcrafted Goods**: Capitalizing on the increasing consumer preference for handcrafted and artisan products over mass-produced items.
2. **E-commerce Expansion**: Utilizing advancements in e-commerce technology to reach a broader audience globally and enhance user experience.
3. **Social Media Marketing**: Leveraging powerful social media platforms and influencer partnerships to increase brand awareness and customer loyalty.
4. **Personalization Trend**: Offering customized products and services to meet the rising demand for personalized shopping experiences.
5. **Artistic Collaboration**: Expanding our product range by collaborating with emerging artists and designers to keep our offerings fresh and exciting.


## Scope

### Project Definition
Niche Art & Toys aims to create an engaging online marketplace for art enthusiasts, collectors, and gift buyers. Our platform will offer handcrafted toys, watercolor paintings, and modern calligraphy pieces, focusing on providing high-quality, unique products.

### Product Range
- **Handcrafted Toys**: Specializing in crochet and fabric toys, perfect for children and collectors.
- **Watercolor Paintings**: Offering original watercolor art, ranging from abstract to realistic styles.
- **Modern Calligraphy Pieces**: Custom and pre-made calligraphy artworks ideal for home decor and gifts.

### Functionalities
- **E-commerce Capabilities**: Complete shopping cart functionality, product searches, user accounts, order management, and payment processing.
- **User Accounts**: Registration, login/logout capabilities, profile management, wishlist and order history.
- **Customer Interaction**: Product rating and comments, contact page.
- **Administration**: Backend functionalities for inventory management.

### Design
- **Responsive Design**: Ensuring the platform is accessible on all devices and screen sizes.
- **User Interface**: Intuitive navigation and attractive layout to enhance user experience.


## Structure
Niche Art & Toys is designed to cater to a diverse user base including art lovers, collectors, and gift buyers. It focuses on creating a user-friendly environment that ensures easy navigation and an intuitive user experience

### User Stories

#### As a Shopper, I want to:
- **View a list of all products** to select items for purchase.
- **Access detailed information on each product** to assess suitability.
- **Identify deals and limited-time offers** to capitalize on discounts.
- **See potential expenditures** to manage budget.
- **Sort products by various attributes** like rating or price to find the best match.
- **Sort through specific categories** to quickly find top products in an area of interest.
- **Search for products by name or description** to locate specific items.
- **See the results of searches and the quantity of matches** to assess options.
- **Select the quantity of a product easily** when making purchases.
- **Review items in the cart before purchasing** to verify the final order.
- **Adjust quantities or remove items in the cart** for last-minute decisions.
- **Enter payment information on a secure page** to ensure data safety.
- **View a summary of the order upon completion** to confirm purchase details.
- **Receive an email confirmation after purchase** to keep a record of the transaction.
- **Add items to a Wishlist** to save for later or monitor price changes.
- **Submit requests for custom art pieces** to acquire personalized art.

#### As a Site User, I want to:
- **Register for an account effortlessly** to create a personalized shopping experience.
- **Log in or out with ease** to access the account without difficulty.
- **Recover passwords smoothly** to regain access to the account if forgotten.
- **Receive confirmation after signing up** to ensure the account is ready.
- **Have a personal user profile** to track orders and save preferences.
- **Access and submit the contact us form easily** to communicate queries or issues.

#### As an Art Enthusiast, I want to:
- **Register for art workshops or events** to engage with the art community and enhance skills.

#### As a Store Owner, I want to:
- **Manage product listings easily** to update inventory with new items, adjust existing listings, or remove outdated products.
- **Promote art events** to build a community around the store and increase customer engagement.


## Skeleton
### Wireframes
#### Home page
<img src="./documentation/wireframes/home_page.png">

#### Main page
<img src="./documentation/wireframes/main_page.png">

#### Product Detail page
<img src="./documentation/wireframes/product_detail.png">

#### Shopping Bag page
<img src="./documentation/wireframes/Shopping_bag.png">

#### Checkout page
<img src="./documentation/wireframes/checkout.png">

#### Mobile wireframes
<img src="./documentation/wireframes/mobile.png">


### User Flow Diagram 

<img src="./documentation/diagrams/user_flow.png">

#### Unregistered User
- Browse products.
- Use the "Contact Us" feature.
- Proceed through checkout to place orders.

#### Registered User
- All capabilities of an unregistered user.
- Manage profile.
- Interact with the wishlist.
- Rate and review products.

#### User Registration (Optional)
- User has the option to register at any point, including during checkout.
- Upon registration, the user's details are saved to `UserProfile`.
- Registered users can add products to their `Wishlist`.
- Users can leave ratings and comments on products.

#### Browsing Products (Both Users)
- Products displayed, sortable and filterable through categories.
- View details of each product.

#### Placing an Order (Both Users)
- Add products to the shopping cart.
- Proceed to checkout:
  - **Unregistered User**: Options to continue as a guest or register. If registering, details can be saved to create a `UserProfile`.
  - **Registered User**: Checkout as usual with an option to update their existing profile details.
- Complete payment process, and create `Order` along with `OrderLineItem` records.

#### Using Contact Us (Both Users)
- All users can send messages through the `Contact` entity regardless of registration status.


### Database Schema
#### Entity Relationship Diagram
<img src="./documentation/diagrams/ERD.png">

#### Category Model

| Field         | Type        | Description                                                |
|---------------|-------------|------------------------------------------------------------|
| name          | CharField   | The official name of the category.                         |
| friendly_name | CharField   | A user-friendly name for the category, optional.           |

#### Product Model

| Field         | Type           | Description                                               |
|---------------|----------------|-----------------------------------------------------------|
| category      | ForeignKey     | Link to the Category model, can be null.                  |
| sku           | CharField      | Stock Keeping Unit, optional.                             |
| name          | CharField      | The name of the product.                                  |
| description   | TextField      | Detailed description of the product.                      |
| is_sold       | BooleanField   | True if the product is sold, false otherwise.             |
| is_clearance  | BooleanField   | True if the product is on clearance, false otherwise.     |
| stock_quantity| IntegerField   | The amount of stock available.                            |
| price         | DecimalField   | Current price of the product.                             |
| old_price     | DecimalField   | Original price of the product before any discounts, optional. |
| rating        | DecimalField   | Average rating of the product, optional.                  |
| image_url     | URLField       | URL of the product image, optional.                       |
| image         | ImageField     | Upload field for the product image, optional.             |

#### Rating Model

| Field        | Type          | Description                                         |
|--------------|---------------|-----------------------------------------------------|
| product      | ForeignKey    | Link to the associated Product.                     |
| user         | ForeignKey    | Link to the User who made the rating.               |
| score        | DecimalField  | The score of the rating.                            |
| comment      | TextField     | Additional comments on the rating, optional.        |
| created_at   | DateTimeField | The date and time when the rating was created.      |

#### Wishlist Model

| Field     | Type          | Description                                          |
|-----------|---------------|------------------------------------------------------|
| user      | ForeignKey    | Link to the User who owns the wishlist.              |
| products  | ManyToManyField | Products included in the wishlist.               |

#### UserProfile Model

| Field                  | Type          | Description                                       |
|------------------------|---------------|---------------------------------------------------|
| user                   | OneToOneField | Link to the Django User model.                    |
| default_full_name      | CharField     | Default full name, optional.                      |
| default_phone_number   | CharField     | Default phone number, optional.                   |
| default_street_address1| CharField     | Default street address, optional.                 |
| default_street_address2| CharField     | Additional default street address, optional.      |
| default_postcode       | CharField     | Default postcode, optional.                       |
| default_town_or_city   | CharField     | Default town or city, optional.                   |
| default_county         | CharField     | Default county, optional.                         |
| default_country        | CountryField  | Default country, optional.                        |


### Surface

#### **Color Scheme:**
Below is the primary color palette used in the project, visually represented:

<img src="./documentation/diagrams/colors.png">

- **Primary body text color**: `#000` - Utilized for main content, ensuring excellent readability against light backgrounds.
- **Button and accent color**: `#4C3957` - A deep, muted purple used for buttons, navigation links, and interactive elements to provide a consistent and elegant interface.
- **Border and active elements color**: `#552C64` - A slightly brighter shade of purple used for borders and active states to subtly distinguish interactive components.
- **Background color for sections**: `#D9DFD8` - A soft gray-green used primarily in backgrounds to create a soothing visual effect and enhance content readability.
- **Text on cards and buttons**: `white` - Ensures high contrast and visibility against darker backgrounds.

#### **Typography:**
- **Primary Font**: `Roboto, sans-serif` - Used extensively throughout the site for its clean, modern appearance. This choice ensures that both body text and headers are legible and aesthetically pleasing.
- **Font Sizes**:
  - General body text follows standard sizing to maintain readability.
  - Headers are scaled appropriately to distinguish section titles from other texts.
- **Special Text Styles**:
  - `.logo-font` - Uppercase transformation for brand-related text to increase impact and recognition.
  - `.text-black` - Applies the primary text color for emphasized text outside the standard body content.

#### **Buttons and Interactive Elements:**
- **Standard Buttons**: Utilize a deep purple background with white text, ensuring they stand out on various backgrounds.
- **Outline Buttons**: Display a white background with a purple border, switching to a purple background on hover or active states to signal interactivity.
- **Icon Usage**: Icons are aligned within buttons and navigation links for visual enhancement and to support user navigation intuitively.

#### **Navigation:**
- **Primary Navigation**: Styled with a background color of `#D9DFD8` to stand out from the main content area. Text and icons in `#4C3957` provide a consistent and accessible user interface.
- **Dropdown Menus**: Utilize the same color palette as the primary navigation for consistency, with items becoming highlighted on hover to improve user experience.

#### **Background and Layout:**
- **Main Background**: Utilizes a full-cover image to create a visually engaging experience right from the start.
- **Content Cards**: Styled with white backgrounds to contrast with the primary purple accents, ensuring that information is easy to read and visually separated from other page elements.

#### **Forms and Inputs:**
- **Form Backgrounds**: Generally maintain a light color to ensure that text inputs are easily visible.
- **Input Fields**: Outlined in the accent color to maintain thematic consistency and visual coherence across form elements.


# E-commerce Application Type
Our platform operates on a Business-to-Consumer (B2C) model, focusing on direct sales between the business and individual consumers. This model is ideal for our niche of handmade crochet toys, used toys, and painted pictures, as it allows us to build personal connections with our customers and provide them with a tailored shopping experience. Here are some characteristics of our B2C model:
- **Direct Interaction**: We engage directly with end users, not businesses, which simplifies the buying process and enhances user experience.
- **Customer Base**: Our primary audience includes gift buyers, parents, collectors, and art enthusiasts who appreciate unique and personalized products.
- **Marketing Strategies**: Tailored to appeal to individual needs and preferences, leveraging targeted advertising, social media engagement, and personalized email campaigns.
- **Customer Support**: Focused on providing excellent customer service to enhance satisfaction and encourage repeat business.
- **Transaction Process**: Designed to be fast and user-friendly, ensuring a seamless checkout experience for all users.

This B2C setup allows us to effectively manage customer relationships and respond quickly to market trends and individual feedback, driving the growth of our online eShop.


# Marketing Strategies

### User Analysis
- **Target Audience**: Gift buyers, parents of young children, collectors, and art enthusiasts.
- **Preferred Platforms**: Etsy, Pinterest, Instagram, Facebook.


### 1. Social Media Marketing
- **Platforms**: Facebook, Twitter, Instagram, Pinterest
- **Activities**: 
  - Regular updates featuring new products and behind-the-scenes content.
  - Seasonal promotions highlighted through Facebook Stories and Pinterest boards.
  - Active community engagement by responding to comments and encouraging shares.

### 2. Content Marketing
- **Method**: Blogging and informative articles.
- **Content Ideas**:
  - "The Art of Crochet: How Our Toys Are Made"
  - "Guide to Caring for Your Handmade Toys"
  - Articles on the benefits of handmade vs. mass-produced toys.
- **Distribution**: Content to be shared across social media platforms and included in email newsletters.

### 3. Email Marketing
- **Strategy**: Use of subscription-based newsletters to engage customers.
- **Features**:
  - Monthly updates on new product launches, behind-the-scenes content, and exclusive offers.
  - Early access to sales and special events for subscribers.

### 4. Influencer Marketing
- **Target**: Parenting bloggers, lifestyle influencers, and artists who align with our brand values.
- **Approach**:
  - Collaborations to showcase real-life uses of our products, enhancing trust and authenticity.

### 5. SEO (Search Engine Optimization)
- **Focus**: On-page optimization and targeting local SEO.
- **Keywords**: "handmade crochet toys", "eco-friendly children's toys", "custom painted pictures".
- **Goal**: Improve search engine rankings to increase organic traffic.

### 6. Paid Advertising
- **Platforms**: Google Ads and Facebook Ads.
- **Types**:
  - Use of retargeting ads to re-engage visitors.
  - Creation of lookalike audiences to expand our customer base.

### 7. Sales Promotions and Discounts
- **Promotions**:
  - Offering seasonal discounts and special holiday sales.
- **Communication**: Promotion details to be announced via social media, email, and on our website.

### Goals and Budget
- **Objectives**: Increase brand visibility, drive online sales, expand the customer base, and build a strong community around our products.
- **Budget Strategy**: Initiate with cost-effective methods like social media and content marketing, scaling into paid advertising as revenue increases.
