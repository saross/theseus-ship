# Verify Semantic Scholar API Key

## Metadata
- **UUID:** `7550e11b-4a12-4830-8cd4-dc595fc4c2c4`
- **URL:** https://claude.ai/chat/7550e11b-4a12-4830-8cd4-dc595fc4c2c4
- **Created:** 2025-02-13 03:56:01
- **Updated:** 2025-02-13 03:56:11
- **Source:** Brian's Claude export

---

## Conversation

### Human (03:56:02)

Can you take these docs and give me a basic curl command to see if my api key works, please? $SEMANTIC_SCHOLAR_API_KEY is the variable

---

### Assistant (03:56:08)

 I'll help you create a simple curl command to test your Semantic Scholar API key. Based on the documentation, we can use the paper details endpoint which is a straightforward GET request.

Here's the curl command:

```bash
curl -H "x-api-key: $SEMANTIC_SCHOLAR_API_KEY" \
     "https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b?fields=title,year"
```

This command:
- Uses the example paper ID from the documentation
- Requests just the title and year fields to keep it simple
- Includes your API key in the header

If your API key is valid, you should receive a JSON response with the paper's title and year. If there's an issue with the API key, you'll receive an error response.

Would you like me to explain what the expected successful response should look like?

---
