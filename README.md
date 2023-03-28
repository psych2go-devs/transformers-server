# transformers-server

Small FastAPI server for HTTP transformers inference

## API

```
POST /cookie
```

### Request

An `application/json` data

| Field        | Description        |
| ------------ | ------------------ |
| `text` (str) | Text for inference |

### Example

```
{
  "text": "I like butter cookies!"
}
```

### Response

An `application/json` data

| Field         | Description               |
| ------------- | ------------------------- |
| `id` (int)    | `0` (`NO`) or `1` (`YES`) |
| `label` (str) | `NO` or `YES`             |

### Example

```
{
  "id": 1,
  "label": "REACT"
}
```

## Environment Variables

| Variable     | Description                             |
| ------------ | --------------------------------------- |
| `MODEL_PATH` | Path to a `distilbert-base-cased` model |

# License

See [LICENSE.md](LICENSE.md)
