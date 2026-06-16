import os

products = [
    {"id": "mens_shoe_1", "category": "mens", "name": "Classic Oxford Leather", "price": "$120.00", "image": "images/mens_shoe_1.png", "desc": "High quality professional product photography of a men's leather oxford dress shoe."},
    {"id": "mens_shoe_2", "category": "mens", "name": "Athletic Runner", "price": "$95.00", "image": "images/mens_shoe_2.png", "desc": "Sleek design, dynamic angle, perfect for daily running."},
    {"id": "mens_shoe_3", "category": "mens", "name": "Casual Slip-on", "price": "$75.00", "image": "images/mens_shoe_3.png", "desc": "Comfortable casual slip-on sneaker for everyday use."},
    {"id": "mens_shoe_4", "category": "mens", "name": "Premium Leather Boot", "price": "$150.00", "image": "images/mens_shoe_4.png", "desc": "Rugged style premium leather boot."},
    {"id": "womens_shoe_1", "category": "womens", "name": "Elegant Stiletto", "price": "$110.00", "image": "images/womens_shoe_1.png", "desc": "Classic design elegant high heel stiletto shoe."},
    {"id": "womens_shoe_2", "category": "womens", "name": "Chic Leather Flat", "price": "$85.00", "image": "images/womens_shoe_2.png", "desc": "Comfortable leather flat shoe with chic design."},
    {"id": "womens_shoe_3", "category": "womens", "name": "Fashion Chunky Sneaker", "price": "$105.00", "image": "images/womens_shoe_3.png", "desc": "Modern aesthetic fashionable chunky sneaker."},
    {"id": "womens_shoe_4", "category": "womens", "name": "Sleek Ankle Boot", "price": "$135.00", "image": "images/womens_shoe_4.png", "desc": "Suede texture sleek ankle boot."},
    {"id": "kids_shoe_1", "category": "kids", "name": "Colorful Athletic Sneaker", "price": "$65.00", "image": "images/kids_shoe_1.png", "desc": "Playful design colorful kids athletic sneaker with velcro straps."},
    {"id": "kids_shoe_2", "category": "kids", "name": "Black School Shoe", "price": "$55.00", "image": "images/kids_shoe_2.png", "desc": "Durable design black leather school shoe."},
    {"id": "kids_shoe_3", "category": "kids", "name": "Summer Sandals", "price": "$45.00", "image": "images/kids_shoe_3.png", "desc": "Comfortable and durable kids summer sandals."},
    {"id": "kids_shoe_4", "category": "kids", "name": "Slip-on Canvas", "price": "$50.00", "image": "images/kids_shoe_4.png", "desc": "Cute pattern kids slip-on canvas shoes."},
    {"id": "accessory_1", "category": "accessories", "name": "Premium Men's Belt", "price": "$40.00", "image": "images/accessory_1.png", "desc": "Premium leather men's belt with classic buckle."},
    {"id": "accessory_2", "category": "accessories", "name": "Shoe Care Kit", "price": "$35.00", "image": "images/accessory_2.png", "desc": "Premium shoe care kit including brush and polish."},
    {"id": "other_1", "category": "others", "name": "Stylish Dress Socks", "price": "$15.00", "image": "images/other_1.png", "desc": "Stylish patterned dress socks."},
    {"id": "other_2", "category": "others", "name": "Premium Insoles", "price": "$25.00", "image": "images/other_2.png", "desc": "Premium leather shoe insoles."}
]

with open("js/products.js", "w", encoding="utf-8") as f:
    f.write("const products = " + str(products).replace("'", '"') + ";\\n")

nav = '''
    <nav class="navbar">
        <div class="container">
            <a href="index.html" class="logo"><img src="images/logo.png" alt="ShoeLogo" style="height:40px;"> ShoeLuxe</a>
            <ul class="nav-links">
                <li><a href="index.html">首頁</a></li>
                <li><a href="about.html">公司簡介</a></li>
                <li><a href="mens.html">男性鞋子</a></li>
                <li><a href="womens.html">女性鞋子</a></li>
                <li><a href="kids.html">童鞋</a></li>
                <li><a href="accessories.html">配件</a></li>
                <li><a href="others.html">其它類</a></li>
                <li><a href="contact.html">聯絡我們</a></li>
            </ul>
        </div>
    </nav>
'''

footer = '''
    <footer class="footer">
        <div class="container">
            <p>&copy; 2026 ShoeLuxe. All rights reserved.</p>
        </div>
    </footer>
'''

css = '''
:root {
    --primary-color: #1a1a1a;
    --secondary-color: #f4f4f4;
    --accent-color: #c99c5f;
    --text-color: #333;
    --bg-color: #fff;
    --font-family: 'Inter', sans-serif;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font-family); color: var(--text-color); background: var(--bg-color); line-height: 1.6; }
.container { width: 90%; max-width: 1200px; margin: 0 auto; }
.navbar { background: var(--primary-color); padding: 1rem 0; color: #fff; position: sticky; top: 0; z-index: 100;}
.navbar .container { display: flex; justify-content: space-between; align-items: center; }
.navbar .logo { color: #fff; text-decoration: none; font-size: 1.5rem; font-weight: bold; display: flex; align-items: center; gap: 10px;}
.navbar .nav-links { list-style: none; display: flex; gap: 15px; }
.navbar .nav-links a { color: #fff; text-decoration: none; padding: 5px 10px; transition: color 0.3s; }
.navbar .nav-links a:hover { color: var(--accent-color); }
.hero { background: var(--secondary-color); padding: 4rem 0; text-align: center; }
.hero h1 { font-size: 3rem; margin-bottom: 1rem; }
.hero p { font-size: 1.2rem; color: #666; margin-bottom: 2rem; }
.btn { display: inline-block; background: var(--primary-color); color: #fff; padding: 10px 20px; text-decoration: none; border-radius: 5px; transition: background 0.3s; cursor: pointer; border: none; font-size: 1rem;}
.btn:hover { background: var(--accent-color); }
.section-title { text-align: center; margin: 3rem 0; font-size: 2rem; }
.products-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-bottom: 3rem; }
.product-card { border: 1px solid #ddd; border-radius: 8px; overflow: hidden; transition: transform 0.3s, box-shadow 0.3s; background: #fff;}
.product-card:hover { transform: translateY(-5px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
.product-card img { width: 100%; height: 250px; object-fit: cover; }
.product-card-body { padding: 1.5rem; text-align: center; }
.product-card h3 { margin-bottom: 0.5rem; }
.product-card .price { color: var(--accent-color); font-weight: bold; font-size: 1.2rem; margin-bottom: 1rem; }
.footer { background: var(--primary-color); color: #fff; text-align: center; padding: 2rem 0; margin-top: 3rem; }
.about, .contact { padding: 4rem 0; text-align: center; }
.contact form { max-width: 600px; margin: 0 auto; display: flex; flex-direction: column; gap: 1rem; }
.contact input, .contact textarea { padding: 10px; border: 1px solid #ddd; border-radius: 5px; font-family: inherit; }
.contact textarea { height: 150px; resize: vertical; }

/* Product Page Specific */
.product-detail { display: flex; gap: 3rem; padding: 4rem 0; align-items: center; }
.product-detail .img-container { flex: 1; }
.product-detail img { width: 100%; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
.product-detail .info { flex: 1; }
.product-detail h1 { font-size: 2.5rem; margin-bottom: 1rem; }
.product-detail .price { font-size: 1.8rem; color: var(--accent-color); font-weight: bold; margin-bottom: 1rem; }
.product-detail p { font-size: 1.1rem; color: #555; margin-bottom: 2rem; }
@media(max-width: 768px) {
    .product-detail { flex-direction: column; }
    .navbar .container { flex-direction: column; gap: 1rem; }
}
'''

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

def get_html(title, body_content):
    return f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - ShoeLuxe</title>
    <link rel="stylesheet" href="css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body>
    {nav}
    {body_content}
    {footer}
    <script src="js/products.js"></script>
    <script src="js/main.js"></script>
</body>
</html>
"""

# Index Page
index_content = '''
    <header class="hero">
        <div class="container">
            <h1>歡迎來到 ShoeLuxe</h1>
            <p>探索我們精心挑選的高品質鞋款與配件</p>
            <a href="mens.html" class="btn">立即選購</a>
        </div>
    </header>
    <div class="container">
        <h2 class="section-title">熱門商品</h2>
        <div class="products-grid" id="featured-products"></div>
    </div>
'''
with open("index.html", "w", encoding="utf-8") as f:
    f.write(get_html("首頁", index_content))

# Category Pages
categories = [
    ("mens", "男性鞋子"),
    ("womens", "女性鞋子"),
    ("kids", "童鞋"),
    ("accessories", "配件"),
    ("others", "其它類")
]

for cat_id, cat_name in categories:
    content = f'''
    <div class="container">
        <h2 class="section-title">{cat_name}</h2>
        <div class="products-grid" id="{cat_id}-products"></div>
    </div>
    '''
    with open(f"{cat_id}.html", "w", encoding="utf-8") as f:
        f.write(get_html(cat_name, content))

# About Page
about_content = '''
    <div class="container about">
        <h2 class="section-title">關於我們</h2>
        <p style="max-width: 800px; margin: 0 auto; font-size: 1.2rem;">ShoeLuxe 致力於為每一位顧客提供最優質、最舒適的鞋履體驗。從設計到製作，我們嚴格把關每一個細節，確保您腳上的每一雙鞋都能完美展現您的獨特風格。</p>
    </div>
'''
with open("about.html", "w", encoding="utf-8") as f:
    f.write(get_html("公司簡介", about_content))

# Contact Page
contact_content = '''
    <div class="container contact">
        <h2 class="section-title">聯絡我們</h2>
        <form>
            <input type="text" placeholder="您的姓名" required>
            <input type="email" placeholder="您的電子郵件" required>
            <textarea placeholder="請輸入您的訊息" required></textarea>
            <button type="button" class="btn" onclick="alert('訊息已送出！')">送出訊息</button>
        </form>
    </div>
'''
with open("contact.html", "w", encoding="utf-8") as f:
    f.write(get_html("聯絡我們", contact_content))

# Product Detail Page
product_content = '''
    <div class="container product-detail" id="product-detail-container">
        <!-- JS will populate this -->
    </div>
'''
with open("product.html", "w", encoding="utf-8") as f:
    f.write(get_html("產品詳情", product_content))

# main.js
js = '''
function createProductCard(product) {
    return `
        <div class="product-card">
            <a href="product.html?id=${product.id}"><img src="${product.image}" alt="${product.name}"></a>
            <div class="product-card-body">
                <h3><a href="product.html?id=${product.id}" style="color: inherit; text-decoration: none;">${product.name}</a></h3>
                <div class="price">${product.price}</div>
                <a href="product.html?id=${product.id}" class="btn">查看詳情</a>
            </div>
        </div>
    `;
}

document.addEventListener('DOMContentLoaded', () => {
    // Populate Featured Products on Index
    const featuredContainer = document.getElementById('featured-products');
    if (featuredContainer) {
        const featured = products.slice(0, 4); 
        featuredContainer.innerHTML = featured.map(createProductCard).join('');
    }

    // Populate Category Pages
    const categories = ['mens', 'womens', 'kids', 'accessories', 'others'];
    categories.forEach(cat => {
        const container = document.getElementById(`${cat}-products`);
        if (container) {
            const catProducts = products.filter(p => p.category === cat);
            container.innerHTML = catProducts.map(createProductCard).join('');
        }
    });

    // Populate Product Detail Page
    const detailContainer = document.getElementById('product-detail-container');
    if (detailContainer) {
        const urlParams = new URLSearchParams(window.location.search);
        const productId = urlParams.get('id');
        const product = products.find(p => p.id === productId);
        
        if (product) {
            detailContainer.innerHTML = `
                <div class="img-container">
                    <img src="${product.image}" alt="${product.name}">
                </div>
                <div class="info">
                    <h1>${product.name}</h1>
                    <div class="price">${product.price}</div>
                    <p>${product.desc}</p>
                    <button class="btn" onclick="alert('已加入購物車！')">加入購物車</button>
                    <a href="javascript:history.back()" class="btn" style="background:#666; margin-left: 10px;">返回</a>
                </div>
            `;
            document.title = `${product.name} - ShoeLuxe`;
        } else {
            detailContainer.innerHTML = '<h2>找不到該產品</h2>';
        }
    }
});
'''

with open("js/main.js", "w", encoding="utf-8") as f:
    f.write(js)
