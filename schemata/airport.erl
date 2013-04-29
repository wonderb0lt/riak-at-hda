{
    schema,
    [
        {version, "1.2"},
        %%{default_field, "title"},
        {default_op, "or"},
        {n_val, 3},
        {analyzer_factory, {erlang, text_analyzers, whitespace_analyzer_factory}}
    ],
    [

        {field, [
            {name, "iata"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},
        {field, [
            {name, "name"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},

        {field, [
            {name, "city"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},

        {field, [
            {name, "terminals"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string} %% Is there a list type? Elsewise I would just remove this

           %% You know, like: ['Terminal A', 'Terminal B', 'Rainbow Dash Commemorational Terminal']
        ]},

        %% A dynamic field. Catches any remaining fields in the
        %% document, and uses the analyzer_factory setting defined
        %% above for the schema.
        {dynamic_field, [
            {name, "*"}
        ]}
    ]
}.
