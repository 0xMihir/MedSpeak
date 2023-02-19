<script lang="ts">
    import SpeechBubble from "$lib/components/SpeechBubble.svelte";
    import Microphone from "svelte-material-icons/Microphone.svelte";
</script>

<div class="left">
    <div class="transcript-wrapper">
        <div id="transcript-content">
            <SpeechBubble content="asdf" left={false} />
            <SpeechBubble content="asdf" left={true} />
        </div>
        <div class="record">
            <button class="record-button">
                <Microphone />
            </button>
        </div>
    </div>
</div>
<div class="right">asdfasdfasdf</div>

<style>
    .left,
    .right {
        flex: 1;
        padding: 24px;
        font-size: 14pt;
        display: flex;
    }

    .transcript-wrapper {
        flex: 1;
        background-color: #1c1d23;
        border-radius: 10px;
        padding: 10px;
        display: flex;
        flex-direction: column;
    }

    #transcript-content {
        flex: 1;
        overflow-y: scroll;
    }

    .record {
        display: flex;
        justify-content: center;
        align-items: center;
        border-top: 2px solid #2c2d33;
        padding-top: 20px;
    }

    .record-button {
        display: flex;
        background-color: #EC625C;
        border: none;
        border-radius: 9999px;
        padding: 15px;
        color: white;
        font-size: 18pt;
        box-shadow: 0px 0px 10px 0px #EC625C;
    }

    .record-button:hover {
        background-color: #ff6860;
        box-shadow: 0px 0px 10px 0px #EC625C;
    }

    .record-button:active {
        background-color: #EC625C;
        box-shadow: 0px 0px 10px 0px #EC625C;
    }
</style>
