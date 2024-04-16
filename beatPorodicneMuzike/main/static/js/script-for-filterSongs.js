document.addEventListener('DOMContentLoaded', function () {
  var filterSelect = document.getElementById('filter-select');
  var songBoxes = document.querySelectorAll('.song');
  var resultCountElement = document.getElementById('result-count');

  filterSelect.addEventListener('change', function () {
    var selectedFilter = filterSelect.value;
    var matchingSongs = [];

    songBoxes.forEach(function (box) {
      var songArtist = box.getAttribute('data-category');
      if (selectedFilter === 'all' || songArtist === selectedFilter) {
        matchingSongs.push(box);
      }
    });

    // Prikazi broj rezultata ispod filtera
    resultCountElement.textContent = matchingSongs.length + ' rezultata';

    // Prikazi ili sakrij pjesme prema odabranoj kategoriji
    songBoxes.forEach(function (box) {
      var shouldDisplay = selectedFilter === 'all' || box.getAttribute('data-category') === selectedFilter;
      box.style.display = shouldDisplay ? 'block' : 'none';
    });
  });
});
