Vue.component('question-box', {
    props: ['question'],
    template: '#question-template',
})

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
        }
    },
    mounted() {
        axios
            .get('/questions/top_ten_last_week/android')
            .then(response => (this.data[0].questions = response.data.result))
        axios
            .get('/questions/ten_newest/android')
            .then(response => (this.data[1].questions = response.data.result))
    },
    filters: {
        timeAgo(timestamp) {
            let m = moment.unix(timestamp);
            return m.fromNow();
        }
    },
});