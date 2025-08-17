document.addEventListener('DOMContentLoaded', () => {

  // ---------- Photography Page Filter ----------
  const filterButtons = document.querySelectorAll('.filter-btn');
  const photoGrid = document.getElementById('photo-grid');

  if (filterButtons.length > 0 && photoGrid) {
    // Load photos from JSON
    fetch('assets/images/photography/photos.json')
      .then(res => res.json())
      .then(data => {
        const categories = Object.keys(data);

        // Create all photo cards
        const allPhotos = [];
        categories.forEach(cat => {
          data[cat].forEach(img => {
            const div = document.createElement('div');
            div.classList.add('photo-card');
            div.dataset.category = cat;
            // Capitalize category for alt text
            const altText = `${cat.charAt(0).toUpperCase() + cat.slice(1)} photo`;
            div.innerHTML = `<img src="assets/images/photography/${img}" alt="${altText}">`;
            allPhotos.push(div);
            photoGrid.appendChild(div);
          });
        });

        // Filter function
        function applyFilter(category) {
          allPhotos.forEach(card => {
            if (card.dataset.category === category) {
              card.style.display = 'block';
              setTimeout(() => card.style.opacity = 1, 10);
            } else {
              card.style.opacity = 0;
              setTimeout(() => card.style.display = 'none', 300);
            }
          });
        }

        // Button click handlers
        filterButtons.forEach(btn => {
          btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            applyFilter(btn.dataset.category);
          });
        });

        // ---------- Default state: Travel ----------
        const defaultCategory = 'travel';
        const defaultButton = document.querySelector(`.filter-btn[data-category="${defaultCategory}"]`);
        if (defaultButton) {
          defaultButton.classList.add('active');
        }
        applyFilter(defaultCategory);
      });
  }

  // ---------- Other JS code for other pages can go here ----------
});
