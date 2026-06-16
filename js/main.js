function createProductCard(product) {
    return `
        <div class="product-card">
            <a href="product.html?id=${product.id}"><img src="${product.image}" alt="${product.name}" title="${product.hover_title}"></a>
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
                    <img src="${product.image}" alt="${product.name}" title="${product.hover_title}">
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
