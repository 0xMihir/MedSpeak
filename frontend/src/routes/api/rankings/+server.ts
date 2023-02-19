import type { RequestHandler } from "./$types";
import { PYTHON_BACKEND_URL } from "$env/static/private";

export const POST = (async ({ request }) => {
    const data = await request.json();
    if (!data || !data.text)
        return new Response(JSON.stringify({ error: "Invalid request" }), { status: 400 });

    const response = await fetch(PYTHON_BACKEND_URL + "/rankings", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: data.text
        })
    });
    return new Response(response.body, {
        headers: {
            "Content-Type": "application/json"
        }
    });
}) satisfies RequestHandler;
