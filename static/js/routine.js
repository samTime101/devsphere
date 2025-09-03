// SEP 3 
// SAMIP REGMI
document.addEventListener('DOMContentLoaded', function () {
    // SELECT ALL TABS
    const tabs = document.querySelectorAll('[data-tab-target]');
    // SELECT ALL TAB CONTENTS
    const tabContents = document.querySelectorAll('.tab-pane'); 

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // GET TARGET CONTENT
            const target = document.querySelector(tab.dataset.tabTarget); 

            // HIDE ALL CONTENTS EXCEPT TARGET
            tabContents.forEach(tc => tc.classList.add('hidden')); 
            target.classList.remove('hidden');

            // RESET ALL TABS AND HIGHLIGHT ACTIVE TAB
            tabs.forEach(t => t.classList.remove('border-blue-500', 'text-white')); 
            tab.classList.add('border-blue-500', 'text-white');
        });
    });
});