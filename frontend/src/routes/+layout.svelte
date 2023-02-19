<script lang="ts">
    import Navbar from "$lib/components/Navbar.svelte";
</script>

<div class="wrapper">
    <Navbar />
    <div class="content">
        <slot />
    </div>
</div>

<style lang="scss">
    .wrapper {
        width: 100%;
        height: 100%;
        display: flex;
        flex-flow: column;
        backdrop-filter: blur(1000px);
    }
    .content {
        display: flex;
        flex: 1;
        flex-direction: row;
        width: 100%;
    }
</style>
