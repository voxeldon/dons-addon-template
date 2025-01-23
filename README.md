# Don's Addon Template

### Requirements:
- Regolith
- Python
- Node.js
- TypeScript

### Getting Started
To initialize the template, run the following command:

```
npm run init_addon
```

### Defining Addon Information
You can define your addon information using a dictionary:

```python
{'author': 'unknown_author', 'pack_id': 'addon_template'}
```

### Full Options
The following options can be defined:

```python
{
    'author': string,          # Author's name
    'pack_id': string,         # Addon identifier
    'version': int[],          # Version as an array of integers
    'engine_version': int[],   # Engine version as an array of integers
    'api_version': string,     # API version
    'ui_api_version': string   # UI API version
}
```

### Other Commands
- `update_manifest` — Increments the manifest number.
- `serialize_animations` — Reads all animation files and generates a single TypeScript JSON containing all animation IDs, lengths, and whether they loop or not.
- `serialize_audio` — Reads all sound ID keys and generates a TypeScript enum containing all sound keys.

---

Let me know if you need further tweaks!