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
            {name, "id"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},

         {field, [
            {name, "type"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]},

        {field, [
            {name, "fop"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]},

        {field, [
            {name, "base"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]},

        {field, [
            {name, "taxes"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]},

        {field, [
            {name, "total"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]},

        {field, [
            {name, "segment"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]},


        {field, [
            {name, "name"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]},
    %% A dynamic field. Catches any remaining fields in the
        %% document, and uses the analyzer_factory setting defined
        %% above for the schema.
        {dynamic_field, [
            {name, "*"}
        ]}
    ]
}.
