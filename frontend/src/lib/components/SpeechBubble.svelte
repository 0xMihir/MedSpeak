<script>
    export let content = "";
    export let left = false;
</script>

<div class="speech-bubble" class:left>
    {content}
</div>

<style lang="scss">
    .speech-bubble {
        border-radius: 15px 15px 15px 0px;
        border: 2px solid #10d3bb;
        padding: 15px;
        width: 50%;
        margin-bottom: 15px;
    }
    .left {
        border: 2px solid #00da76;
        border-radius: 15px 15px 0px 15px;
        margin-left: auto;
    }
</style>
