<script>

</script>

<div class="card">
    <slot />
</div>

<style lang="scss">
    .card {
        border-radius: 15px;
        background-color: #1c1d23;
        border: 2px solid #2c2d33;
        padding: 15px;
        width: 80%;
        margin-bottom: 15px;
        :global(h2) {
            margin-top: 0;
            margin-bottom: 10px;
            text-align: center;
        }
    }
</style>