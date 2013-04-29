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
            {name, "booking"}, %% Reference to booking key?
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},

        {field, [
            {name, "vendor"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},

        {field, [
            {name, "date"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, date}
        ]},

        {field, [
            {name, "departure"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, date}
        ]},

        {field, [
            {name, "arrival"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, date}
        ]},

        {field, [
            {name, "airline"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},

        {field, [
            {name, "from"}, %% Reference to airport key
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		      {type, string}
        ]},

        {field, [
            {name, "to"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},


        {field, [
            {name, "Stops"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string} %% list of stops. since we don't know what stops look like, no idea.
        ]},


        {field, [
            {name, "duration"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, date}
        ]},


        {field, [
            {name, "status"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},


        {field, [
            {name, "aircraft"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
		   {type, string}
        ]},

        {field, [
            {name, "eTicket"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]},


        {field, [
            {name, "seat"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
            {type, string}
        ]},


        {field, [
            {name, "services"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string} %% list of strings
        ]},

        {field, [
            {name, "baggage"},
            {analyzer_factory, {erlang, text_analyzers, noop_analyzer_factory}},
           {type, string}
        ]},

        {field, [
            {name, "class"},
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
