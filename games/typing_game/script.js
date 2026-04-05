// AICE 코드 타자 연습 게임 로직

class TypingGame {
    constructor() {
        this.currentCategory = null;
        this.currentCodes = [];
        this.currentIndex = 0;
        this.correctCount = 0;
        this.incorrectCount = 0;
        this.streak = 0;
        this.maxStreak = 0;
        this.startTime = null;
        this.totalTime = 0;
        this.isPlaying = false;
        this.codeStartTime = null;
        this.records = this.loadRecords();
        this.toggleStates = this.loadToggleStates();
        
        this.init();
    }
    
    init() {
        this.targetCodeEl = document.getElementById('targetCode');
        this.codeInputEl = document.getElementById('codeInput');
        this.liveFeedbackEl = document.getElementById('liveFeedback');
        this.codeDescriptionEl = document.getElementById('codeDescription');
        this.codePronunciationEl = document.getElementById('codePronunciation');
        this.codeGrammarEl = document.getElementById('codeGrammar');
        this.timerEl = document.getElementById('timer');
        this.accuracyEl = document.getElementById('accuracy');
        this.streakEl = document.getElementById('streak');
        this.progressFillEl = document.getElementById('progressFill');
        this.progressTextEl = document.getElementById('progressText');
        this.gameAreaEl = document.getElementById('gameArea');
        this.startScreenEl = document.getElementById('startScreen');
        this.resultModal = document.getElementById('resultModal');
        this.codeCountEl = document.getElementById('codeCount');
        
        this.descSection = document.getElementById('descSection');
        this.pronSection = document.getElementById('pronSection');
        this.grammarSection = document.getElementById('grammarSection');
        this.toggleDescBtn = document.getElementById('toggleDesc');
        this.togglePronBtn = document.getElementById('togglePron');
        this.toggleGrammarBtn = document.getElementById('toggleGrammar');
        
        this.createCategoryButtons();
        this.codeInputEl.addEventListener('input', () => this.handleInput());
        this.codeInputEl.addEventListener('keydown', (e) => this.handleKeydown(e));
        this.displayRecords();
        this.displayTotalCodeCount();
        this.applyToggleStates();
    }
    
    loadToggleStates() {
        const saved = localStorage.getItem('aice_typing_toggles');
        return saved ? JSON.parse(saved) : { desc: true, pron: true, grammar: true };
    }
    
    saveToggleStates() {
        localStorage.setItem('aice_typing_toggles', JSON.stringify(this.toggleStates));
    }
    
    applyToggleStates() {
        if (this.toggleStates.desc) {
            this.descSection.classList.remove('hidden');
            this.toggleDescBtn.classList.add('active');
        } else {
            this.descSection.classList.add('hidden');
            this.toggleDescBtn.classList.remove('active');
        }
        if (this.toggleStates.pron) {
            this.pronSection.classList.remove('hidden');
            this.togglePronBtn.classList.add('active');
        } else {
            this.pronSection.classList.add('hidden');
            this.togglePronBtn.classList.remove('active');
        }
        if (this.toggleStates.grammar) {
            this.grammarSection.classList.remove('hidden');
            this.toggleGrammarBtn.classList.add('active');
        } else {
            this.grammarSection.classList.add('hidden');
            this.toggleGrammarBtn.classList.remove('active');
        }
    }
    
    toggleSection(section) {
        this.toggleStates[section] = !this.toggleStates[section];
        this.saveToggleStates();
        this.applyToggleStates();
    }
    
    displayTotalCodeCount() {
        let total = 0;
        categories.forEach(key => { total += codeData[key].codes.length; });
        this.codeCountEl.textContent = `총 ${total}개 코드 패턴`;
    }
    
    createCategoryButtons() {
        const container = document.getElementById('categoryButtons');
        container.innerHTML = '';
        const allBtn = document.createElement('button');
        allBtn.className = 'category-btn';
        allBtn.dataset.category = 'all';
        allBtn.innerHTML = '🎯 전체';
        allBtn.onclick = () => this.selectCategory('all');
        container.appendChild(allBtn);
        
        categories.forEach(key => {
            const cat = codeData[key];
            const btn = document.createElement('button');
            btn.className = 'category-btn';
            btn.dataset.category = key;
            btn.innerHTML = `${cat.icon} ${cat.name} <span class="count">(${cat.codes.length})</span>`;
            btn.onclick = () => this.selectCategory(key);
            container.appendChild(btn);
        });
    }
    
    selectCategory(category) {
        document.querySelectorAll('.category-btn').forEach(btn => {
            btn.classList.remove('active');
            if (btn.dataset.category === category) btn.classList.add('active');
        });
        this.currentCategory = category;
        if (category === 'all') {
            this.currentCodes = [];
            categories.forEach(key => { this.currentCodes.push(...codeData[key].codes); });
        } else {
            this.currentCodes = [...codeData[category].codes];
        }
        this.shuffleArray(this.currentCodes);
        this.currentCodes = this.currentCodes.slice(0, 10);
    }
    
    shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }
    
    startGame() {
        if (!this.currentCategory) { alert('카테고리를 먼저 선택해주세요!'); return; }
        this.currentIndex = 0;
        this.correctCount = 0;
        this.incorrectCount = 0;
        this.streak = 0;
        this.maxStreak = 0;
        this.totalTime = 0;
        this.isPlaying = true;
        this.startTime = Date.now();
        this.startScreenEl.style.display = 'none';
        this.gameAreaEl.style.display = 'block';
        this.showNextCode();
        this.timerInterval = setInterval(() => this.updateTimer(), 100);
        this.codeInputEl.focus();
    }
    
    showNextCode() {
        if (this.currentIndex >= this.currentCodes.length) { this.endGame(); return; }
        const item = this.currentCodes[this.currentIndex];
        this.targetCodeEl.textContent = item.code;
        this.codeDescriptionEl.textContent = item.desc || '';
        this.codePronunciationEl.textContent = item.pron || '';
        this.codeGrammarEl.textContent = item.grammar || '';
        this.codeInputEl.value = '';
        this.codeInputEl.className = '';
        this.liveFeedbackEl.innerHTML = this.generateFeedbackHTML('', item.code);
        this.codeStartTime = Date.now();
        this.updateProgress();
    }
    
    handleInput() {
        debbuger;
        if (!this.isPlaying) return;
        const input = this.codeInputEl.value;
        const target = this.currentCodes[this.currentIndex].code;
        this.liveFeedbackEl.innerHTML = this.generateFeedbackHTML(input, target);
        let isCorrectSoFar = true;
        for (let i = 0; i < input.length; i++) {
            if (input[i] !== target[i]) { isCorrectSoFar = false; break; }
        }
        if (input.length === 0) this.codeInputEl.className = '';
        else if (isCorrectSoFar) this.codeInputEl.className = 'correct';
        else this.codeInputEl.className = 'incorrect';
    }
    
    generateFeedbackHTML(input, target) {
        let html = '';
        for (let i = 0; i < target.length; i++) {
            if (i < input.length) {
                if (input[i] === target[i]) html += `<span class="correct-char">${this.escapeHtml(target[i])}</span>`;
                else html += `<span class="incorrect-char">${this.escapeHtml(target[i])}</span>`;
            } else html += `<span class="pending-char">${this.escapeHtml(target[i])}</span>`;
        }
        return html;
    }
    
    escapeHtml(char) {
        const map = { '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;', "'": '&#039;', ' ': '&nbsp;' };
        return map[char] || char;
    }
    
    handleCorrect() {
        this.correctCount++;
        this.streak++;
        if (this.streak > this.maxStreak) this.maxStreak = this.streak;
        this.updateStats();
        this.currentIndex++;
        setTimeout(() => this.showNextCode(), 300);
    }
    
    handleKeydown(e) {
        if (e.key === 'Tab') { e.preventDefault(); if (this.isPlaying) this.skipCode(); }
        if (e.key === 'Escape') { if (this.isPlaying) this.endGame(); }
        if (e.key === 'Enter') {
            const input = this.codeInputEl.value;
            const target = this.currentCodes[this.currentIndex].code;
            if (input === target) this.handleCorrect();
          }
    }
    
    skipCode() {
        this.incorrectCount++;
        this.streak = 0;
        this.currentIndex++;
        this.updateStats();
        this.showNextCode();
    }
    
    updateTimer() {
        if (!this.isPlaying) return;
        const elapsed = (Date.now() - this.startTime) / 1000;
        this.timerEl.textContent = elapsed.toFixed(1) + 's';
    }
    
    updateStats() {
        const total = this.correctCount + this.incorrectCount;
        const accuracy = total > 0 ? Math.round((this.correctCount / total) * 100) : 100;
        this.accuracyEl.textContent = accuracy + '%';
        this.streakEl.textContent = this.streak;
        if (this.streak >= 3) {
            this.streakEl.parentElement.classList.add('streak-bonus');
            setTimeout(() => this.streakEl.parentElement.classList.remove('streak-bonus'), 500);
        }
    }
    
    updateProgress() {
        const progress = (this.currentIndex / this.currentCodes.length) * 100;
        this.progressFillEl.style.width = progress + '%';
        this.progressTextEl.textContent = `${this.currentIndex} / ${this.currentCodes.length}`;
    }
    
    endGame() {
        this.isPlaying = false;
        clearInterval(this.timerInterval);
        this.totalTime = (Date.now() - this.startTime) / 1000;
        const total = this.correctCount + this.incorrectCount;
        const accuracy = total > 0 ? Math.round((this.correctCount / total) * 100) : 0;
        document.getElementById('resultCorrect').textContent = this.correctCount;
        document.getElementById('resultAccuracy').textContent = accuracy + '%';
        document.getElementById('resultTime').textContent = this.totalTime.toFixed(1) + 's';
        document.getElementById('resultStreak').textContent = this.maxStreak;
        this.resultModal.classList.add('show');
        this.saveRecord(accuracy, this.totalTime);
    }
    
    closeModal() { this.resultModal.classList.remove('show'); this.resetGame(); }
    
    resetGame() {
        this.gameAreaEl.style.display = 'none';
        this.startScreenEl.style.display = 'block';
        this.codeInputEl.value = '';
        this.codeInputEl.className = '';
        if (this.currentCategory) this.selectCategory(this.currentCategory);
    }
    
    saveRecord(accuracy, time) {
        const categoryName = this.currentCategory === 'all' ? '전체' : codeData[this.currentCategory].name;
        const record = { category: categoryName, accuracy: accuracy, time: time.toFixed(1), date: new Date().toLocaleDateString() };
        this.records.unshift(record);
        this.records = this.records.slice(0, 10);
        localStorage.setItem('aice_typing_records', JSON.stringify(this.records));
        this.displayRecords();
    }
    
    loadRecords() {
        const saved = localStorage.getItem('aice_typing_records');
        return saved ? JSON.parse(saved) : [];
    }
    
    displayRecords() {
        const container = document.getElementById('recordsList');
        if (this.records.length === 0) { container.innerHTML = '<p style="color: #666; text-align: center;">아직 기록이 없습니다</p>'; return; }
        container.innerHTML = this.records.map(r => `<div class="record-item"><span class="category">${r.category}</span><span class="score">${r.accuracy}% / ${r.time}s</span></div>`).join('');
    }
    
    clearRecords() {
        if (confirm('모든 기록을 삭제하시겠습니까?')) {
            this.records = [];
            localStorage.removeItem('aice_typing_records');
            this.displayRecords();
        }
    }
}

let game;
document.addEventListener('DOMContentLoaded', () => { game = new TypingGame(); });
function startGame() { game.startGame(); }
function closeModal() { game.closeModal(); }
function restartGame() { game.closeModal(); game.startGame(); }
function clearRecords() { game.clearRecords(); }
function toggleSection(section) { game.toggleSection(section); }
