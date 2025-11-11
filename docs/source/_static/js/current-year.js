document.addEventListener('DOMContentLoaded', () => {
  const start = 2020;
  const year = new Date().getFullYear();
  if (year === start) return;
  const re = new RegExp(`${start}(-\\d{4})?`, 'g');
  document.querySelectorAll('body *').forEach(el => {
    if (el.children.length === 0 && el.textContent && re.test(el.textContent)) {
      el.textContent = el.textContent.replace(re, `${start}-${year}`);
    }
  });
});
