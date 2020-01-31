Vue.component('question-box', {
    props: ['question'],
    template: '#question-template',
    filters: {
        timeAgo(timestamp) {
            let m = moment.unix(timestamp);
            return m.fromNow();
        }
    },
})

Vue.component('expand-trigger-btn', {
    template: '#expand-trigger-btn-template',
});

Vue.component('post-content', {
    props: ['post'],
    template: '#post-template',
    filters: {
        timeAgo(timestamp) {
            let m = moment.unix(timestamp);
            return m.fromNow();
        }
    },
});

Vue.component('expand-modal', {
    props: ['question'],
    template: '#expand-modal-template',
    data() {
        return {
            question_id: this.question.question_id,
            answers: [],
        }
    },
    mounted() {
        axios
            .get(`/answers/${this.question_id}`)
            .then(response => (this.answers = response.data.result))
    },
});

Vue.component('expand-btn', {
    props: ['question'],
    template: '#expand-btn-template',
    data() {
        return { showModal: false }
    },
});

new Vue({
    el: '#questions',
    data() {
        return {
            data: [
                {
                    title: "10 Most Voted Questions in Last Week",
                    questions: [],
                },
                {
                    title: "10 Newest Questions",
                    questions: [],
                },
            ],
            tag: 'android',
        }
    },
    mounted() {
        axios
            .get(`/questions/top_ten_last_week/${this.tag}`)
            .then(response => (this.data[0].questions = response.data.result))
        axios
            .get(`/questions/ten_newest/${this.tag}`)
            .then(response => (this.data[1].questions = response.data.result))
    },
});