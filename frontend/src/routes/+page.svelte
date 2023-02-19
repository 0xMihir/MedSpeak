<script lang="ts">
    import SpeechBubble from "$lib/components/SpeechBubble.svelte";
    import Card from "$lib/components/Card.svelte";
    import Microphone from "svelte-material-icons/Microphone.svelte";
    import { onMount } from "svelte";
    import { writable } from "svelte/store";
    import LineChart from "$lib/components/LineChart.svelte";

    let transcript = [
        {
            speaker: "Doctor",
            content: "Hello, how are you feeling today?"
        },
        {
            speaker: "Patient",
            content:
                "I'm not feeling well, I'm very tired all the time and my breathing has been a bit difficult lately."
        },
        {
            speaker: "Doctor",
            content: "I see. Can you tell me more about your symptoms? When did they start?"
        },
        {
            speaker: "Patient",
            content:
                "I've been feeling tired for a few weeks now and it's been hard to breathe for about a month. I also have a dry cough that won't go away."
        },
        {
            speaker: "Doctor",
            content: "Have you experienced any chest pain or discomfort?"
        },
        {
            speaker: "Patient",
            content: "No, not really. Just the difficulty breathing and the cough."
        },
        {
            speaker: "Doctor",
            content: "Okay. Do you have any joint pain or swelling?"
        },
        {
            speaker: "Patient",
            content: "Actually, I have had some swelling in my ankles."
        },
        {
            speaker: "Doctor",
            content: "Have you noticed any rashes or skin changes?"
        },
        {
            speaker: "Patient",
            content: "No, not that I'm aware of."
        },
        {
            speaker: "Doctor",
            content:
                "Alright, based on your symptoms, I want to do some tests to check for a condition called Sarcoidosis. It's a rare condition that can cause the symptoms you're experiencing. Have you heard of it before?"
        },
        {
            speaker: "Patient",
            content: "No, I haven't."
        },
        {
            speaker: "Doctor",
            content:
                "Sarcoidosis is a condition where small clumps of inflammatory cells, called granulomas, form in different parts of the body, such as the lungs, lymph nodes, and skin. It can cause fatigue, cough, shortness of breath, and swelling in the ankles, like you mentioned. We will need to run some tests to confirm the diagnosis."
        },
        {
            speaker: "Patient",
            content: "What kind of tests?"
        },
        {
            speaker: "Doctor",
            content:
                "We'll start with a chest x-ray and some blood tests. Depending on the results, we may also need to do a biopsy of one of the affected organs."
        },
        {
            speaker: "Patient",
            content: "Okay, I understand."
        },
        {
            speaker: "Doctor",
            content:
                "Don't worry, we'll do everything we can to get you feeling better. Let's get those tests scheduled and we'll go from there."
        }
    ];

    const data = writable({
        conditions: {
            data: {},
            rankings: []
        },
        observations: {
            data: {},
            rankings: []
        },
        medications: {
            data: {},
            rankings: []
        },
        encounters: {
            data: {},
            rankings: []
        },
        procedures: {
            data: {},
            rankings: []
        }
    });

    onMount(async () => {
        data.set(
            await (
                await fetch("/api/rankings", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        text: transcript.map((t) => t.content).join(" ")
                    })
                })
            ).json()
        );
    });

    const orderData = (data: any, rankings: number[], maxResults = 5) => {
        const orderedData = new Map();
        if (maxResults) rankings = rankings.slice(0, maxResults);
        rankings.forEach((rank) => {
            const key = Object.keys(data)[rank];
            orderedData.set(key, data[key]);
        });
        return orderedData;
    };

    const orderDates = (data: { date: string }[]) => {
        return data
            .sort((a, b) => {
                return new Date(b.date).getTime() - new Date(a.date).getTime();
            })
            .map((d) => {
                return new Date(d.date).toLocaleDateString("en-US", {
                    year: "numeric",
                    month: "long",
                    day: "numeric"
                });
            });
    };
</script>

<div class="left">
    <div class="transcript-wrapper">
        <h2>Transcript</h2>
        <div id="transcript-content">
            {#each transcript as t}
                <SpeechBubble left={t.speaker == "Patient"}>
                    {t.content}
                </SpeechBubble>
            {/each}
        </div>
        <div class="record">
            <button class="record-button">
                <Microphone />
            </button>
        </div>
    </div>
</div>

<div class="right">
    <h1>Conditions</h1>
    <div class="card-panel">
        {#key $data}
            {#each [...orderData($data.conditions.data, $data.conditions.rankings)] as [condition, date]}
                <Card>
                    <h2>{condition}</h2>
                    <ul>
                        {#each orderDates(date) as d}
                            <li>{d}</li>
                        {/each}
                    </ul>
                </Card>
            {/each}
        {/key}
    </div>
    <h1>Observations</h1>
    <div class="card-panel">
        {#key $data}
            {#each [...orderData($data.observations.data, $data.observations.rankings)] as [observation, value]}
                <Card>
                    <h2>{observation}</h2>
                    <LineChart data={value} xLabel="Date" yLabel={observation.split("[")[0]} />
                </Card>
            {/each}
        {/key}
        <h1>Medications</h1>
        {#key $data}
            {#each [...orderData($data.medications.data, $data.medications.rankings)] as [medication, date]}
                <Card>
                    <h2>{medication}</h2>
                    {#if date.length < 10}
                        <ul>
                            {#each orderDates(date) as d}
                                <li>{d}</li>
                            {/each}
                        </ul>
                    {:else}
                        <ul>
                           <li>
                            Prescribed {date.length} times between {new Date(date[0].date).toLocaleDateString("en-US", {
                                year: "numeric",
                                month: "long",
                                day: "numeric"
                            })} and {new Date(date[date.length - 1].date).toLocaleDateString("en-US", {
                                year: "numeric",
                                month: "long",
                                day: "numeric"
                            })}
                           </li>
                        </ul>
                    {/if}
                </Card>
            {/each}
        {/key}
        <h1>Visitations</h1>
        {#key $data}
            {#each [...orderData($data.encounters.data, $data.encounters.rankings)] as [visitation, date]}
                <Card>
                    <h2>{visitation}</h2>
                    {#if date.length < 10}
                        <ul>
                            {#each orderDates(date) as d}
                                <li>{d}</li>
                            {/each}
                        </ul>
                    {:else}
                        <ul>
                           <li>
                            {date.length} visits between {new Date(date[0].date).toLocaleDateString("en-US", {
                                year: "numeric",
                                month: "long",
                                day: "numeric"
                            })} and {new Date(date[date.length - 1].date).toLocaleDateString("en-US", {
                                year: "numeric",
                                month: "long",
                                day: "numeric"
                            })}
                           </li>
                        </ul>
                    {/if}
                </Card>
            {/each}
        {/key}
        <h1>Procedures</h1>
        {#key $data}
            {#each [...orderData($data.procedures.data, $data.procedures.rankings)] as [procedure, date]}
                <Card>
                    <h2>{procedure}</h2>
                    <ul>
                        {#each orderDates(date) as d}
                            <li>{d}</li>
                        {/each}
                    </ul>
                </Card>
            {/each}
        {/key}
    </div>
</div>

<style lang="scss">
    .left,
    .right {
        flex: 1;
        padding: 24px;
        font-size: 14pt;
        display: flex;
        min-height: 0;
        flex-direction: column;
    }

    .right {
        overflow-y: scroll;
        margin: 20px 0;
        padding: 10px;

        h1 {
            margin-top: 0;
        }
    }

    .transcript-wrapper {
        flex: 1;
        background-color: #1c1d23;
        border-radius: 10px;
        padding: 10px;
        display: flex;
        flex-direction: column;
        height: 100%;
        min-height: 0;
        h2 {
            margin-top: 0;
            margin-bottom: 10px;
            text-align: center;
        }
    }

    #transcript-content {
        border-top: 2px solid #2c2d33;
        padding: 24px 24px 0 24px;
        flex: 1;
        overflow-y: scroll;
        min-height: 0;
    }

    .record {
        display: flex;
        justify-content: center;
        align-items: center;
        border-top: 2px solid #2c2d33;
        padding-top: 24px;
    }

    .record-button {
        display: flex;
        background-color: #ec625c;
        border: none;
        border-radius: 9999px;
        padding: 15px;
        color: white;
        font-size: 18pt;
        box-shadow: 0px 0px 10px 0px #ec625c;
    }

    .record-button:hover {
        background-color: #ff6860;
        box-shadow: 0px 0px 10px 0px #ec625c;
    }

    .record-button:active {
        background-color: #ec625c;
        box-shadow: 0px 0px 10px 0px #ec625c;
    }
</style>
