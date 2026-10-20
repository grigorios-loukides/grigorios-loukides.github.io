'use strict';
const normalise = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
const matches = (record, query, year, type, source) => (!year || record.year === year) && (!type || record.type === type) && (!source || record.sources.includes(source)) && query.split(/\s+/).every(word => record.text.includes(word));
if (typeof module !== 'undefined') module.exports = {normalise, matches};
if (typeof document !== 'undefined') {
  document.documentElement.classList.add('js');
  const rows = Array.from(document.querySelectorAll('.pub'));
  const data = rows.map(row => ({text: normalise(row.textContent), year: row.dataset.year, type: row.dataset.type, sources: row.dataset.sources.split('|')}));
  const search = document.getElementById('search'), year = document.getElementById('year'), type = document.getElementById('type'), source = document.getElementById('source');
  const more = document.getElementById('more');
  let limit = 25;
  function render(reset = true) {
    if (reset) limit = 25;
    const query = normalise(search.value.trim());
    let count = 0, shown = 0;
    rows.forEach((row, i) => {
      const match = matches(data[i], query, year.value, type.value, source.value);
      if (match) count++;
      row.hidden = !match || count > limit;
      if (!row.hidden) shown++;
    });
    document.getElementById('count').textContent = `${shown} of ${count} matching records · ${rows.length} in the catalogue`;
    document.getElementById('empty').hidden = count > 0;
    more.hidden = shown >= count;
    more.textContent = `Show ${Math.min(25, count - shown)} more`;
  }
  search.addEventListener('input', () => render());
  [year, type, source].forEach(input => input.addEventListener('change', () => render()));
  more.addEventListener('click', () => {limit += 25; render(false);});
  document.getElementById('reset').addEventListener('click', () => {search.value = ''; year.value = ''; type.value = ''; source.value = ''; render(); search.focus();});
  render();
}
